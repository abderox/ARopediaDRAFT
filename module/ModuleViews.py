from datetime import datetime, date
from modulefinder import Module
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from numpy import int16
from module.models import *
from semestre.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def add_module(request):
    semestres = Semestre.objects.all()
    return render(request, "modules/add_module_template.html",{"semestres":semestres})


@login_required
def add_module_save(request):
    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    else:
        module_libelle = request.POST.get("module")
        semestre_id = request.POST.get("semestre_id")
        #semestre = Semestre.objects.all()[semestre_id]
        semestre = Semestre.objects.get(id=semestre_id)
        try:
            course = Module.objects.create(
                libelle_module=module_libelle, semestre=semestre)
            course.save()
            messages.success(request, "Le module est ajouté avec succès !")
            return HttpResponseRedirect(reverse(add_module))

        except:
            messages.error(request, "Echec d'ajout du module !")
            return HttpResponseRedirect(reverse(add_module))


@login_required
def  add_element_module(request):
    modules = Module.objects.all()
    profs = Professeur.objects.all()
    prerequis = ElementModule.objects.all()
    return render(request,"modules/add_elem_module_template.html",{"profs":profs , "modules": modules , "element_modules":prerequis}) 


@login_required
def add_element_module_save(request):
    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    else:
        libelle_element_module = request.POST.get("libelle_element_module")
        module_id = request.POST.get("module_id")
        prerequis_id = request.POST.getlist("prerequis_id")
        volumeHoraire = request.POST.get("volumeHoraire")
        objectif = request.POST.get("objectif")
        prof_id = request.POST.getlist("prof")
        module = Module.objects.get(id=module_id)
        responsable = request.POST.get("responsable") 
        
        # prof = Professeur.objects.get(id=1) 
        # # preqd = ElementModule.objects.get(id=14) 
       
        # element_module.prof_id.add(prof)
        #prere = Perequis.objects.create(element_module_id=element_module, prerequis_id=preqd)   

        try:
            
            
            respo = Professeur.objects.get(id=responsable)     
            element_module = ElementModule.objects.create(libelle_element_module=libelle_element_module, volumeHoraire=volumeHoraire,
                                                            objectif=objectif,
                                                            module=module,responsable=respo)
            
            for pr in prof_id:
                prof = Professeur.objects.get(id=pr)
                element_module.prof_id.add(prof)
                element_module.save()
            #     element_module = ElementModule.objects.create(libelle_element_module=libelle_element_module, volumeHoraire=volumeHoraire,
            #                                               objectif=objectif,
            #                                               module=module, prof_id=prof)
            # element_module = ElementModule.objects.create(libelle_element_module=libelle_element_module, volumeHoraire=volumeHoraire,
            #                                                 objectif=objectif,
            #                                                 module=module, prof_id=prof)
            
            
            for preq in prerequis_id:
                preqd = ElementModule.objects.get(id=int(preq))  
                d = Perequis.objects.create(element_module_id=element_module, prerequis_id=preqd)   
                d.save() 
                                                                  
            

            
                
            
            
          
            messages.success(request, "L'élément de module est ajouté avec succès !")
            return HttpResponseRedirect(reverse(add_element_module))

        except:

            messages.error(request, "Echec au niveau d'ajout de l'element de module ! ")
            return HttpResponse(prof_id)




@login_required
def edit_element_module_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method is Not Allowed</h2>")
    else:
        libelle_element_module = request.POST.get("libelle_element_module")
        module_id = request.POST.get("module_id")
        element_id = request.POST.get("element_id")
        prerequis_id = request.POST.getList("prerequis_id")
        volumeHoraire = request.POST.get("volumeHoraire")
        objectif = request.POST.get("objectif")
        prof_id = request.POST.get("prof")

        try:
            module = Module.objects.get(id=module_id)
            prerequis =ElementModule.objects.get(id=prerequis_id)
            prof = Professeur.objects.get(id=prof_id)
            element_module = ElementModule.objects.get(id=element_id)
            
            element_module.libelle_element_module=libelle_element_module
            element_module.volumeHoraire=volumeHoraire
            element_module.objectif=objectif
            element_module.module_id=module
            element_module.prof_id=prof
            
            
            prerequis_ = Perequis.objects.get(id=prerequis)
            prerequis_.element_module_id=element_module
            prerequis_.prerequis_id=prerequis
            element_module.save()
            prerequis_.save()

            messages.success(request,"L'élément de module est modifié avec succès")
            return HttpResponse(reverse("edit_module",kwargs={"element_id":element_id}))
        except:
            messages.error(request, "Echec au niveau de modifier l'element de module ! ")
            return HttpResponseRedirect(reverse(add_element_module))


@login_required
def edit_module_save(request):
    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    else:
        module_libelle = request.POST.get("module")
        semestre_id = request.POST.get("semestre_id")
        module_id = request.POST.get("module_id")
        #semestre = Semestre.objects.all()[semestre_id]
        semestre = Semestre.objects.get(id=semestre_id)
        try:
            course = Module.objects.get(id=module_id)
            course.libelle_module=module_libelle
            course.semestre=semestre
            course.save()
            messages.success(request, "Le module est modifié avec succès !")
            return HttpResponseRedirect(reverse(manage_modules))

        except:
            messages.error(request, "Echec de la modification !")
            return HttpResponseRedirect(reverse(manage_modules))



@login_required
def manage_modules(request):
    modules = Module.objects.all()
    page = request.GET.get('page', 1)
    
    paginator = Paginator(modules, 30)
    try:
        modules_ = paginator.page(page)
    except PageNotAnInteger:
        modules_ = paginator.page(1)
    except EmptyPage:
        modules_ = paginator.page(paginator.num_pages)
        
    return render(request, "modules/manage_modules.html", {"modules": modules_})

@login_required
def manage_elem_modules(request):
    elem_modules = ElementModule.objects.all()

    return render(request, "modules/manage_elem_modules.html", {"elem_modules": elem_modules })

@login_required
def delete_module(request,id_):
    try:
        Module.objects.filter(id=id_).delete()
        messages.success(request, "Le module est supprimé avec succès !")
        return HttpResponseRedirect(reverse(manage_modules))
    except:
        messages.error(request, "Echec de la suppression !")
        return HttpResponseRedirect(reverse(manage_modules))
    

@login_required    
def delete_elem_module(request,id_):
    ElementModule.objects.filter(id=id_).delete()
    return HttpResponseRedirect(reverse(manage_elem_modules))

@login_required
def edit_module(request,id_):
    semestres = Semestre.objects.all()
    module = Module.objects.get(id=id_)
    return render(request, "modules/edit_module_template.html",{"module":module,"semestres":semestres})
