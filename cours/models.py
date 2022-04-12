from django.db import models
from module.models import ElementModule


class Chapitre(models.Model):
    libelle = models.CharField(null = False )
    Document = models.ForeignKey(Document , null=True,  on_delete= models.SET_NULL)


class Document(models.Model):
    titre = models.CharField(max_length=40,null = False )
    type = models.CharField(max_length=20,null = False )
    path = models.CharField(max_length=100,null = False )

class Modele3D(models.Model):
    path = models.CharField(max_length=100,null = False )


class Image(models.Model):
    type = models.CharField(max_length=20,null = False )
    path = models.CharField(max_length=100,null = False )


class Traitement(models.Model):
    titre = models.CharField(max_length=40,null = False )
    label = models.CharField(max_length=100,null = False )
    chapitre = models.ForeignKey(Chapitre , null=True,  on_delete= models.SET_NULL)
    image = models.ForeignKey(Image , null=True,  on_delete= models.SET_NULL)
    modele3D = models.ForeignKey(Modele3D , null=True,  on_delete= models.SET_NULL)



    


# Create your models here.
