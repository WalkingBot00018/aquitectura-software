from django.db import models

# Create your models here.
class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    Nombre=models.TextField(null=True,verbose_name='Nombre')
    Apellido=models.TextField(verbose_name='Apellido')
    NumeroTelefono=models.BigIntegerField(null=True,verbose_name='NumeroTelefono')
    direccion=models.TextField(null=True,verbose_name='Direccion')

