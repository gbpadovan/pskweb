from django.shortcuts import render, redirect

from item.models import Categoria, Produto
from .forms import SignupForm

# Create your views here.
def index(request):
    produtos = Produto.objects.filter(em_estoque=True)[0:6]
    categorias = Categoria.objects.all()

    return render(
        request, 
        "core/index.html",
        {
            'categorias':categorias,
            'produtos': produtos,
        },                 
    )

def contato(request):
    return render(request, "core/contato.html")

def cadastrar(request):
    if request.method=="POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/entrar/")
    else:
        form = SignupForm()

    return render(
        request, 
        "core/cadastrar.html",
        {
            'form':form
        },                 
    )

def sobre(request):
    return render(request, "core/sobre.html")

def termos(request):
    return render(request, "core/termos.html")

"""
def experimental(request):
    produtos = Produto.objects.filter(em_estoque=True)[0:6]
    categorias = Categoria.objects.all()

    return render(
        request, 
        "core/base2.html",
        {
            'categorias':categorias,
            'produtos': produtos,
        },                 
    )
"""