from django.db import models
from .user import User

class Account(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= 'Id Inmueble')
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE, verbose_name='Usuario')
    Casa_Apartamento = models.CharField(max_length=100, verbose_name='Casa o apartamento')
    Venta_arriendo = models.CharField(max_length=50, verbose_name='Venta o arriendo')
    Superficie = models.CharField(max_length=250, verbose_name='Superficie')
    Nueva_Usada = models.CharField(max_length=250, verbose_name='Nueva o usada')
    Precio = models.IntegerField(verbose_name='Precio')
