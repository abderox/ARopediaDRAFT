from operator import mod
from django.db import models
from semestre.models import Semestre
from users.models import Professeur


class Module(models.Model):
    id = models.AutoField(primary_key=True)
    libelle_module = models.CharField(max_length=200, null=True)
    semestre = models.ForeignKey(Semestre, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libelle_module
        

class ElementModule(models.Model):
    id = models.AutoField(primary_key=True)
    libelle_element_module = models.CharField(max_length=200,null=True)
    volumeHoraire = models.IntegerField(null=False)
    objectif = models.TextField()
    module = models.ForeignKey(Module, null=True, on_delete=models.CASCADE)
    prof_id = models.ManyToManyField(Professeur)
    responsable = models.OneToOneField(Professeur,on_delete=models.DO_NOTHING, related_name='%(class)s_responsable',null=True)
    # perequis = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libelle_element_module

class Perequis(models.Model):
    id = models.AutoField(primary_key=True)
    element_module_id = models.ForeignKey(ElementModule,null=False, blank=False , on_delete=models.CASCADE , related_name='%(class)s_element_module')
    prerequis_id =models.ForeignKey(ElementModule,null=False, blank=False , on_delete=models.CASCADE , related_name='%(class)s_prerequis')
    
    
    
    
    
    
    
    
    
