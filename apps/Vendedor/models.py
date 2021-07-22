from django.db import models
from django.db.models.fields import CharField, EmailField, IntegerField

# Create your models here.

NIVELES_ESTUDIOS = (
    ('Educación Basica', 'Educación Basica'),
    ('Educación Media', 'Educación Media'),
    ('Educación Superior', 'Educación Superior'),
)

class Vendedor (models.Model):
    
    rut = CharField(max_length=10, blank=False)
    nombre = CharField(max_length=50)
    email = EmailField(max_length=100, blank=True)
    telefono = CharField(max_length=15)
    sueldo = IntegerField()
    nivel_estudio = CharField(max_length=50, choices=NIVELES_ESTUDIOS)
    
    def __str__(self):
        return self.nombre