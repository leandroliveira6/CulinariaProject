from django.shortcuts import render, redirect  # , get_list_or_404, get_object_or_404
from .models import Receita
from django.contrib import auth
from django.core.files.storage import FileSystemStorage

from django.utils.text import get_valid_filename


def index(request):
    # get_list_or_404(Receita, visible=True)
    receitas = Receita.objects.filter(visible=True)
    return render(request, 'index.html', {'receitas': receitas})


def minhas_receitas(request):
    # get_list_or_404(Receita, visible=True)
    receitas = Receita.objects.filter(owner_user=auth.get_user(request))
    return render(request, 'index.html', {'receitas': receitas})


def detail(request, id):
    # get_object_or_404(Receita, pk=id)
    receita = Receita.objects.get(pk=id)
    return render(request, 'detail.html', {'receita': receita})


def search(request):
    # get_list_or_404(Receita, name__contains=request.GET.get('search', ''))
    receitas = Receita.objects.filter(
        name__contains=request.GET.get('search', ''))
    return render(request, 'index.html', {'receitas': receitas})

def nova_receita(request):
    if(request.method == 'POST'):
        print(request.FILES)
        name = request.POST.get('name', '')
        ingredients = request.POST.get('ingredients', '')
        steps = request.POST.get('steps', '')
        time = request.POST.get('time', '')
        category = request.POST.get('category', '')
        picture = request.FILES.get('picture', '')
        picture.name = get_valid_filename(picture.name)
        Receita.objects.create(name=name, ingredients=ingredients, steps=steps, time=time, category=category, picture=picture, owner_user=auth.get_user(request))
        return redirect('index')
        
    return render(request, 'nova_receita.html')

def mudar_visibilidade(request, id):
    receita = Receita.objects.get(pk=id)
    receita.visible = not receita.visible
    receita.save()
    return redirect('detail', id=id)
