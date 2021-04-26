# Ejemplo de como ejecutar un script de python dentro del Proyecto
# Simplemente importamos toda la libreria wsgi y usamos todos los modulo y libreria del proyecto
# Con esta idea voy a hacer las importaciones del viejo sistema

from core.wsgi import *

from tablas.models import Aula

aula = Aula.objects.all()

for n in aula:
    print(n)