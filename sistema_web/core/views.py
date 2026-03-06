# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.db.models import Q # Importação para buscar por Nome OU Código
# from .forms import ProdutoForm
# from .models import Produtos


# #Tela inicial (menu) - Só entra se tivwr logado

# @login_required
# def home(request):
#     return render(request, 'core/home.html')

# @login_required
# # sistema_web/core/views.py

# @login_required
# def cadastrar_produto(request):
#     produtos_encontrados = [] #a tabela vai iniciar vazio por padrão
#     termo_busca = request.GET.get('q')
#     tipo_busca = request.GET.get('tipo_busca')

#     # SE TIVER BUSCA: Filtra pelo termo
#     if termo_busca:
#         if tipo_busca == 'codigo':
#             produtos_encontrados = Produtos.objects.filter(codigodebarra__icontains=termo_busca)[:50]
#         else:
#             produtos_encontrados = Produtos.objects.filter(descricao__icontains=termo_busca)[:50]
    
#     # uma melhoria futura SE NÃO TIVER BUSCA: Mostra os últimos 20 produtos cadastrados (para a tabela não sumir)
#     else:
#         # Tenta ordenar pelo ID (indice) decrescente para pegar os novos
#         # Se seu campo ID tiver outro nome, ajuste o '-indice'
#         produtos_encontrados = Produtos.objects.all().order_by('-indice')[:10]
        

#     # Lógica de salvar o formulário
#     if request.method == 'POST':
#         form = ProdutoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, '✅ Salvo com sucesso!')
#             return redirect('cadastro')
#         else:
#             messages.error(request, '⚠️ Erro ao salvar. Verifique se todos os campos obrigatórios foram preenchidos.')
#             print(form.errors)
#     else:
#         form = ProdutoForm()
    
#     aba_ativa = 'busca' if termo_busca else 'cadastro' #garante que a aba busca renderize e mantenha nela

#     return render(request, 'core/cadastro.html', {
#         'form': form,
#         'produtos': produtos_encontrados, # Agora sempre tem dados
#         # 'termo_ativar_aba': 'busca' if termo_busca else 'cadastro'
#         'active_tab': aba_ativa # ativando a aba_ativa
#     })


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max 
from .forms import ProdutoForm
from .models import Produtos

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
# sistema_web/core/views.py

@login_required
def cadastrar_produto(request):
    produtos_encontrados = []
    termo_busca = request.GET.get('q')
    tipo_busca = request.GET.get('tipo_busca')

    # Lógica de Busca
    if termo_busca:
        if tipo_busca == 'codigo':
            produtos_encontrados = Produtos.objects.filter(codigodebarra__icontains=termo_busca)[:50]
        else:
            produtos_encontrados = Produtos.objects.filter(descricao__icontains=termo_busca)[:50]
    else:
        produtos_encontrados = Produtos.objects.all().order_by('-indice')[:10]

    # === LÓGICA DE SALVAR INTELIGENTE ===
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            # commit=False significa: "Cria o produto, mas NÃO salva no banco ainda!"
            produto = form.save(commit=False) 
            
            # Busca o maior número de indice atual no banco
            maior_indice = Produtos.objects.aggregate(Max('indice'))['indice__max']
            
            # Se o banco estiver vazio, começa no 1. Se não, pega o maior e soma 1.
            produto.indice = (maior_indice or 0) + 1 
            
            # Agora sim, salva no banco definitivamente com o indice preenchido!
            produto.save() 
            
            messages.success(request, f'✅ Produto cadastrado com sucesso! (ID Gerado: {produto.indice})')
            return redirect('cadastro')
        else:
            messages.error(request, '⚠️ Erro ao salvar. Verifique os dados.')
            print(form.errors)
    else:
        form = ProdutoForm()
    
    aba_ativa = 'busca' if termo_busca else 'cadastro'

    return render(request, 'core/cadastro.html', {
        'form': form,
        'produtos': produtos_encontrados,
        'active_tab': aba_ativa
    })