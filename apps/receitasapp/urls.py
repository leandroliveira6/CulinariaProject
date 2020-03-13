from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('q', views.search, name='search'),
    path('nova-receita', views.nova_receita, name='nova-receita'),
    path('minhas-receitas', views.minhas_receitas, name='minhas-receitas'),
    path('mudar-visibilidade/<int:id>', views.mudar_visibilidade, name='mudar-visibilidade'),
]
