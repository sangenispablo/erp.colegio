from django.shortcuts import render
from django.views.generic import ListView

from tablas.models import Aula


# Vista basada en Funcion
def aula_list(request):
    context = {
        'segment': 'tabla-aula',
        'obj': Aula.objects.all()
    }
    return render(request, 'aula/aula_list.html', context=context)


# Vista basada en Clase
class AulaListView(ListView):
    model = Aula
    template_name = 'aula/aula_list.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'tabla-aula'
        return context
