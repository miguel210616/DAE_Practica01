from django.db import models

# Create your models here.

class Region(models.Model):
    nombre_region=models.CharField(max_length=50)

class Candidato(models.Model):
    region=models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre_candidato=models.CharField(max_length=50)
    votos=models.IntegerField(default=0)


