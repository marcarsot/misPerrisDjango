from django.db import models
from django.utils import timezone

class Socios(models.Model):
    TIPO_VIVIENDA = [
        (1, 'Casa con patio grande'),
        (2, 'Casa con patio pequeño'),
        (3, 'Casa sin patio'),
        (4, 'Departamento')
    ]

    rut = models.CharField(max_length=11, verbose_name= 'RUT' )
    nombre = models.CharField(max_length=50, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    email = models.EmailField(max_length=130, verbose_name='Correo')
    telefono = models.CharField(max_length=20, verbose_name='Tu Numero')
    direccion = models.CharField(max_length=100)
    fec_nac = models.DateField()
    vivienda = models.IntegerField(choices=TIPO_VIVIENDA)

    def __str__(self) -> str:
        return super().__str__()

