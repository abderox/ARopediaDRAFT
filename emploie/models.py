from email.headerregistry import Group
from operator import imod
from tokenize import group
from django.db import models
from semestre.models import Groupe
from users.models import Professeur


class Salle(models.Model):
    nom_salle =  models.CharField(max_length=100, null=True) 
    disponible = models.BooleanField()

class TypeSalle(models.Model):
    capacite =  models.IntegerField(max_length=100) 
    libelle =   models.CharField(max_length=100, null=True) 

class Presence(models.Model):
    libelle = models.CharField(max_length=100, null=True) 

class Planning(models.Model):
    liblle =  models.CharField(max_length=100, null=True) 
    groupe = models.ForeignKey(Groupe , null = True , on_delete= models.SET_NULL )
    salle = models.ForeignKey(Salle , null = True , on_delete= models.SET_NULL )
    professeur = models.ForeignKey(Professeur , null = True , on_delete= models.SET_NULL )
    # element de module 

class Seance(models.Model):
    date_debut = models.DateTimeField(null = False )
    date_fin = models.DateTimeField(null = False )
    planning = models.OneToOneField(Planning, null = True , on_delete= models.SET_NULL)















  

