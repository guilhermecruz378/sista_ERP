from django import forms
from .models import Produtos

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        # fields = '__all__'
        exclude = ['indice']
        
        widgets = {
            # Mantém os campos bonitos que já tínhamos
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'codigodebarra': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo': forms.TextInput(attrs={'class': 'form-control'}),
            
            # --- A MÁGICA ACONTECE AQUI ---
            # Transformamos o campo 'validade' num calendário nativo
            'validade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }