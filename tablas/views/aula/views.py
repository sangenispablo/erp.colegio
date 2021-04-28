from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView

from tablas.models import Aula, Nivel
from tablas.forms import AulaForm


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

    # Tanto este dispatch como el post son de pruebas
    # se probo el envio de Json y sin csrf
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            nivel = Nivel.objects.get(pk=request.POST['id']).toJSON()
            data = nivel
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'tabla-aula'
        return context


class AulaCreateView(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = ''