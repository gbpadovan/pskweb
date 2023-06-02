from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path("", views.index, name='index'),
    path("contato/", views.contato, name="contato"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path(
        "entrar/", 
        auth_views.LoginView.as_view(
            template_name = 'core/entrar.html',
            authentication_form=LoginForm,
            ), 
        name='entrar'
    ),
    path('sair/', auth_views.LogoutView.as_view(next_page='/'), name='sair'),
    path("sobre/", views.sobre, name="sobre"),
    path("termos/", views.termos, name="termos"),
]