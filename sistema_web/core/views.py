from django.shortcuts import render, redirect, get_object_or_404 
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
    # === AUTO-CURA DE PRODUTOS CORROMPIDOS (SEM DELETAR) ===
    # Procura todos os produtos que estão com o índice vazio no banco
    produtos_quebrados = Produtos.objects.filter(indice__isnull=True)
    
    if produtos_quebrados.exists():
        # Acha o maior número que existe hoje
        maior_indice = Produtos.objects.aggregate(Max('indice'))['indice__max'] or 0
        
        for prod in produtos_quebrados:
            maior_indice += 1
            # Usa o .update() para injetar o índice novo direto na linha corrompida do banco!
            Produtos.objects.filter(
                codigodebarra=prod.codigodebarra, 
                descricao=prod.descricao
            ).update(indice=maior_indice)
    # ========================================================

    
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


@login_required
def editar_produto(request, indice):
    # Busca o produto usando a coluna indice
    produto = get_object_or_404(Produtos, indice=indice)

    # 2. Se o usuário clicou no botão "Salvar" após alterar os dados
    if request.method == 'POST':
        # O "instance=produto" é a mágica: diz ao Django que é um UPDATE e não um novo cadastro!
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Produto {produto.codigodebarra} atualizado com sucesso no banco!')
            return redirect('cadastro')
    else:
        # 3. Se ele só clicou no "Lápis", carrega o formulário com os dados do banco preenchidos
        form = ProdutoForm(instance=produto)

    # Reutilizamos a mesma tela de cadastro! Forçamos a aba 'cadastro' a abrir.
    return render(request, 'core/cadastro.html', {
        'form': form,
        'active_tab': 'cadastro'
    })

@login_required
def excluir_produto(request, indice):
    # 1. Puxa do banco
    produto = get_object_or_404(Produtos, indice=indice)
    nome_produto = produto.descricao # Salva o nome para a mensagem
    
    # 2. Exclui permanentemente do banco de dados
    produto.delete()
    
    # 3. Avisa o usuário e volta para a tela de cadastro
    messages.success(request, f'🗑️ O produto "{nome_produto}" foi excluído do banco de dados.')
    return redirect('cadastro')

@login_required
def dashboard(request):
    # Renderiza a tela do dashboard
    return render(request, 'core/dashboard.html')