from django.shortcuts import render

# Create your views here.
def showDemoPage(request):
    return render(request,"users/login.html")

def add_module(request):
    return render(request, "modules/add_module_template.html")

