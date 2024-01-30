from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from market.conversation.forms import ConversationMessageForm
from market.conversation.models import Conversation
from market.item.models import Item


@login_required
def new_conversation(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if item.created_by == request.user:
        return redirect('dashboard')
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation_detail', pk=conversations.first().id)
        pass
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('conversation_detail', pk=item.pk)
    else:
        form = ConversationMessageForm()

    context = {
        'form': form,
        'item': item
    }
    return render(
        request,
        'conversation/new.html',
        context,
    )


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    context = {
        'conversations': conversations
    }
    return render(
        request,
        'conversation/inbox.html',
        context
    )


@login_required
def conversation_detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('conversation_detail', pk=conversation.pk)
    else:
        form = ConversationMessageForm()

    context = {
        'conversation': conversation,
        'form': form
    }

    return render(request,
                  'conversation/conversation_detail.html',
                  context)
