from django import forms
from .models import Produto


INPUT_CSS_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    """ """
    class Meta:
        model = Produto
        fields = (
            'categoria', 'nome', 'marca', 'modelo',
            'tamanho', 'unid_por_embalagem', 'descrição', 'preço',
            'imagem', 'em_estoque',
        )
        widgets = {
            'categoria':forms.Select(attrs={'class':INPUT_CSS_CLASSES}),
            'nome':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'marca':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'modelo':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'tamanho':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'unid_por_embalagem':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'descrição':forms.Textarea(attrs={'class':INPUT_CSS_CLASSES}),  
            'preço':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'imagem':forms.FileInput(attrs={'class':INPUT_CSS_CLASSES}),             
        }


class EditItemForm(forms.ModelForm):
    """ """
    class Meta:
        model = Produto
        fields = (
            'categoria', 'nome', 'marca', 'modelo',
            'tamanho', 'unid_por_embalagem', 'descrição', 'preço',
            'imagem', 'em_estoque',
        )
        widgets = {
            'nome':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'marca':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'modelo':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'tamanho':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'unid_por_embalagem':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'descrição':forms.Textarea(attrs={'class':INPUT_CSS_CLASSES}),  
            'preço':forms.TextInput(attrs={'class':INPUT_CSS_CLASSES}), 
            'imagem':forms.FileInput(attrs={'class':INPUT_CSS_CLASSES}),             
        }


