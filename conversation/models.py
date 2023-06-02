from django.contrib.auth.models import User
from django.db import models

from item.models import Produto


class Conversa(models.Model):
    produto = models.ForeignKey(Produto, related_name='conversations', on_delete=models.CASCADE)
    membros = models.ManyToManyField(User, related_name='conversations')
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modificado_em',)


class ConversaMensagem(models.Model):
    conversa = models.ForeignKey(Conversa, related_name='messages', on_delete=models.CASCADE)    
    content = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    