from django.shortcuts import render

def index(request):
  return render(request, 'index.html', {'receitas': ['Sopa de letrinhas', 'Feijoada', 'Pizza'] })

def receita(request):
  return render(request, 'receita.html')