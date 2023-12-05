from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.

def hello(request):
    return HttpResponse("Hello, world = olá mundo ")

def amz(request):
    return render(request, 'usuario/home.html')

def cadastro(request):
    novo_item = Produto()
    novo_item.nome = request.POST.get('nome')
    novo_item.idade = request.POST.get('idade')
    novo_item.save()

    #mostra todos os itens 
    produtos = {
        'produtos' : Produto.objects.all()
    }

    #listagem de itens
    return render(request, 'usuario/itens.html', produtos)