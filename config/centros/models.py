from django.db import models

# Create your models here.

from django.db import models

class Sede(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class Ambiente(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    capacidad = models.IntegerField()
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

    def __str__(self):
        return f"Aula {self.codigo}"


class Instructor(models.Model):
    documento = models.CharField(max_length=20, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    ambientes = models.ManyToManyField(Ambiente)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

