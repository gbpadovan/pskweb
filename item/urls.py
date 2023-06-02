from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.procurar, name='procurar'),
    path('novo_produto/', views.novo_produto, name='novo_produto'),
    path('<int:pk>/', views.detalhe, name='detalhe'), # a string 'detalhe' representa um path que vai ser representado pela string '<int:pk>/' e vai apontar para item/views.py function detalhe  
    path('<int:pk>/delete_produto', views.delete_produto, name='delete_produto'),
    path('<int:pk>/edite_produto', views.edite_produto, name='edite_produto')
]