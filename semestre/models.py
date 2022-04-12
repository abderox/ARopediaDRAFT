from django.db import models

from users.models import Etudiant
from filiere.models import Filiere


# Create your models here.


class Niveau(models.Model):
    nom_niveau = models.CharField(max_length=100, null=True)
    type_niveau = models.CharField(max_length=100, null=True)
    filliere = models.ForeignKey(Filiere , null=True,  on_delete= models.SET_NULL )



class Groupe(models.Model):
    nom_group = models.CharField(max_length=100, null=True)
    niveau = models.ForeignKey(Niveau ,  null=True,  on_delete= models.SET_NULL)



class AnneUniversitaire(models.Model):
    group = models.ForeignKey(Groupe , null=True,  on_delete= models.SET_NULL )
    etudiant = models.ForeignKey(Etudiant , null=True,  on_delete= models.SET_NULL)
    libelle = models.CharField(max_length=100, null=True)
    date = models.DateField(null = False )


class Semestre(models.Model):
    libelle_semestre = models.CharField(max_length=100, null=True) 
    niveau = models.ForeignKey(Niveau ,  null=True , on_delete= models.SET_NULL )

# ajouter foreign key qui pointe sur fillière  au semetre
