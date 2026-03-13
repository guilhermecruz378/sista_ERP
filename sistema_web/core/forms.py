from django import forms
from .models import Produtos

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        exclude = ['indice'] # Deixa o índice para o auto-incremento
        
        # Como a data precisa de um calendário, a gente avisa o Django aqui
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }

    # TRUQUE DE MESTRE: Aplica a classe CSS 'form-control' em TODOS os campos automaticamente
def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Preserva as classes que já existem (como o type date) e adiciona o form-control
            classes_atuais = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{classes_atuais} form-control'.strip()
        