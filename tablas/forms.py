from django.forms import ModelForm

from tablas.models import Aula


class AulaForm(ModelForm):
    class Meta:
        model = Aula
        fields = ['nivel', 'turno', 'curso', 'division', 'detalle']
