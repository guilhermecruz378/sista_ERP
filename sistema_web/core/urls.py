from django.urls import path
from . import views

urlpatterns = [
    # Sua rota atual:
    path('', views.cadastrar_produto, name='cadastro'),
    
    # NOVAS ROTAS PARA EDITAR E EXCLUIR:
    # O "<int:indice>" avisa o Django que vamos passar o ID do produto pela URL
    path('cadastro/editar/<int:indice>/', views.editar_produto, name='editar_produto'),
    path('cadastro/excluir/<int:indice>/', views.excluir_produto, name='excluir_produto'),

    path('dashboard/', views.dashboard, name='dashboard'),

]