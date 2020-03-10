from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita


def index(request):
    receitas = get_list_or_404(Receita)
    return render(request, 'index.html', {'receitas': receitas})


def receita(request, id):
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receita.html', {'receita': receita})
