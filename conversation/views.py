from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from item.models import Produto
from .models import Conversa
from .forms import ConversaMensagemForm

@login_required
def new_conversation(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if produto.cadastrado_por == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversa.objects.filter(produto=produto).filter(membros__in=[request.user.id])
    #print(conversations)

    if conversations:
        return redirect('conversation:detail.html', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversaMensagemForm(request.POST)
        #print(form)       
        if form.is_valid():
            # atualiza o db
            #print('form id valid')
            conversation = Conversa.objects.create(produto=produto)
            conversation.membros.add(request.user)
            conversation.membros.add(produto.cadastrado_por)
            conversation.save()

            # form            
            conversation_message = form.save(commit=False)  # commit=False não salva direto no db          
            conversation_message.conversa = conversation            
            conversation_message.criado_por = request.user            
            conversation_message.save()                     # após cadastrar conversa e criado_por, agora pode salvar o form

            return redirect('item:detalhe', pk=produto_id)
        
    else:
        form = ConversaMensagemForm()        

    return render(request, 'conversation/new.html',{
        'form':form,
        'produto':produto,
    })


@login_required
def inbox(request):
    conversations = Conversa.objects.filter(membros__in=[request.user.id])

    return render(request, 'conversation/inbox.html',{
        'conversations':conversations,
    })


@login_required
def detail(request, pk):
    conversation = Conversa.objects.filter(membros__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversaMensagemForm(request.POST)

        if form.is_valid(): 
            # form            
            conversation_message = form.save(commit=False)  # commit=False não salva direto no db          
            conversation_message.conversa = conversation            
            conversation_message.criado_por = request.user            
            conversation_message.save()                     # após cadastrar conversa e criado_por, agora pode salvar o form
            conversation.save()                             # salva a conversa para modificar a data
            
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversaMensagemForm()

    return render(request, 'conversation/detail.html',{
        'conversation':conversation,
        'form': form,
    })