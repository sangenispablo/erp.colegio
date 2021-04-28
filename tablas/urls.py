from django.urls import path

from tablas.views.aula.views import AulaListView, AulaCreateView, aula_list

urlpatterns = [
    path('aula/', AulaListView.as_view(), name='aula-list'),
    path('aula/create/', AulaCreateView.as_view(), name='aula-create'),
    # path('aula/', aula_list, name='aula-list'),
]
