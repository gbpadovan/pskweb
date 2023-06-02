from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from item.models import Produto


@login_required
def index(request):
    produtos = Produto.objects.filter(cadastrado_por=request.user)

    return render(request, 'dashboard/index.html', {
        'produtos':produtos,
    })

