from django.contrib import admin
from semestre.models import *
from users.models import Professeur
from filiere.models import *
# Register your models here.
admin.site.register(Professeur)
admin.site.register(Niveau)
admin.site.register(Semestre)
admin.site.register(Filiere)
admin.site.register(Etablissement)
