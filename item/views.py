from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Categoria
from .forms import NewItemForm, EditItemForm


def procurar(request):
    """mostra todos os produtos do db que não foram vendidos"""
    query = request.GET.get('query', '')
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria', 0)     # quando a pessoa fizer um request vai ter na url a palavra 'categoria'. Este script vai pegar o conteúdo desta parte da url, ou vai devolver o default=0
    produtos = Produto.objects.filter(em_estoque=True)

    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)

    if query:
        # model "Produto" has an entity called "nome"
        # syntax:
        #   produtos.filter(entity__icontains=query)
        produtos = produtos.filter(
            Q(nome__icontains=query) | Q(descrição__icontains=query)
        )

    return render(request, 'item/procurar.html', {
        "produtos":    produtos,
        "query":       query,
        "categorias":  categorias,
        "categoria_id":int(categoria_id),
    })


def detalhe(request, pk):
    """
    <request>
    <pk> primary key
    """
    produto = get_object_or_404(Produto, pk=pk)
    # vai mostrar até 3 produtos relacionados:
    itens_relacionados = Produto.objects.filter(categoria=produto.categoria, em_estoque=True).exclude(pk=pk)[0:3]

    return render(
        request, 
        "item/detalhe.html",
        {
            "produto": produto,
            "itens_relacionados": itens_relacionados,  
        }                 
    )

@login_required
def novo_produto(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # cadastra novo produto no db
            produto = form.save(commit=False)
            produto.cadastrado_por = request.user
            produto.save() 

            return redirect('item:detalhe', pk=produto.id)
    else:
        form = NewItemForm()

    return render(
        request, 
        "item/cad_produto.html",
        {
            "form": form,
            "title": "Novo Produto"
        }                 
    )
    
@login_required
def delete_produto(request, pk):
    """deleta o produto da db"""
    produto = get_object_or_404(Produto, pk=pk, cadastrado_por=request.user)
    produto.delete()

    return redirect("dashboard:index")


@login_required
def edite_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk, cadastrado_por=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=produto)

        if form.is_valid():
            # atualiza formulário no db
            form.save()

            return redirect('item:detalhe', pk=produto.id)

    else:
        form = EditItemForm(instance=produto)

    return render(
        request, 
        "item/edite_produto.html",
        {
            "form": form,
            "produto":produto,
            "title": "Edite Produto"
        }                 
    )
