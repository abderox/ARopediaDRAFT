from django.db import models
import datetime
import time

# Create your models here.
def upload_location(instance, filename):
        filebase, extension = filename.split('.')
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        return 'filiere_images/%s.%s' % (str(stamp), extension)


class Etablissement(models.Model):
    nom = models.CharField(max_length=100, null=True)
    adress = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=20, null=True)
    logo = models.ImageField(upload_to=upload_location)
    def __str__(self):
        return self.nom


class Filiere(models.Model):
    nom_filiere = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=upload_location)
    etablissement = models.ForeignKey(Etablissement , null=True,  on_delete= models.SET_NULL)
    def __str__(self):
        return self.nom_filiere
