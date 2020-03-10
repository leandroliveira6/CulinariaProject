from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita


def index(request):
    receitas = Receita.objects.filter(visible=True) # get_list_or_404(Receita, visible=True)
    return render(request, 'index.html', {'receitas': receitas})


def detail(request, id):
    receita = Receita.objects.filter(pk=id) # get_object_or_404(Receita, pk=id)
    return render(request, 'receita.html', {'receita': receita})


def search(request):
    receitas = Receita.objects.filter(name__contains=request.GET.get('search', '')) # get_list_or_404(Receita, name__contains=request.GET.get('search', ''))
    return render(request, 'index.html', {'receitas': receitas})
