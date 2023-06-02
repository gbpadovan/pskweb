from django import forms

from .models import ConversaMensagem


class ConversaMensagemForm(forms.ModelForm):
    class Meta:
        model = ConversaMensagem
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border',
            })
        }