from operator import mod
from django.db import models
from semestre.models import Semestre
from users.models import Professeur

class Module(models.Model):
    libelle_module = models.CharField(max_length=200, null=True)
    semestre = models.ForeignKey(Semestre , null=True, on_delete= models.SET_NULL)

class ElementModule(models.Model):
    volumeHoraire = models.IntegerField(null = False )
    objectif = models.CharField(max_length=500 , null = False )
    module = models.ForeignKey(Module,null=True, on_delete= models.SET_NULL)
    perequis = models.ManyToManyField('self', related_name="perequises" , symmetrical=False  )


class Enseignant_Responsable(models.Model):
    enseignant = models.ForeignKey(Professeur,null=True, on_delete= models.SET_NULL)
    element_module = models.ForeignKey(ElementModule ,null=True, on_delete= models.SET_NULL)
    is_responsable = models.BooleanField(null = False  )
    annee_universitaire = models.DateField(null = False )