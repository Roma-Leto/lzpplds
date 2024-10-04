from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from users.models import User
from .forms import MessageForm
from django.db.models import Q


@login_required
def chat_view(request, recipient_id):
    recipient = User.objects.get(pk=recipient_id)
    messages = Message.objects.filter(
        Q(sender=request.user, recipient=recipient) |
        Q(sender=recipient, recipient=request.user)
    ).order_by('timestamp')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('chat:chat', recipient_id=recipient_id)
    else:
        form = MessageForm()
        context = {
            'recipient': recipient,
            'messages': messages,
            'form': form
        }
    return render(request, 'chat/chat.html', context)
