from django.urls import path

from tablas.views.aula.views import AulaListView, aula_list

urlpatterns = [
    path('aula/', AulaListView.as_view(), name='aula-list'),
    # path('aula/', aula_list, name='aula-list'),
]
