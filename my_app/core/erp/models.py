from django.db import models
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")
    
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ["id"]

class Employee(models.Model):
    
    #type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name="Nombres")
    dni = models.CharField(max_length=10, unique=True, verbose_name="dni")
    date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")
    date_creation = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    cvitae = models.FileField(upload_to="cvitae/%Y/%m/%d", null=True, blank=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleado"
        ordering = ["id"]

    def __str__(self):
        return self.names