from django.shortcuts import render
from . models import Message
# Create your views here.
def index(request):
    context = {}
    return render(request, 'chatapp/index.html', context)

def detail(request,pk):
    context = {}
    return render(request, 'chatapp/detail.html', context)

from django.contrib.auth.models import User

def chat_with_friend(request, friend_name):
    friend = User.objects.get(username=friend_name)
    
    if request.method == "POST":
        message_content = request.POST['message']
        
   
        Message.objects.create(sender=request.user, content=message_content)
      
    messages = Message.objects.filter(sender=request.user, read_by=friend) | Message.objects.filter(sender=friend, read_by=request.user)
    messages = messages.order_by('created_at')

    return render(request, 'chatapp/chat_detail.html', {
        'friend_name': friend_name,
        'messages': messages,
        'detail_title': f"Chat with {friend_name}",
        'detail_description': f"Start the conversation with {friend_name}!",
    })
