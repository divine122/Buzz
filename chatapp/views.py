from django.shortcuts import render,get_object_or_404, redirect
from . models import UserProfile,Friend,Message,ChatRoom
from .forms import MessageForm

# Create your views here.




def index(request):
    if not request.user.is_authenticated:
        return render(request, 'chatapp/index.html', {'user': None, 'friends': []})
    
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
 
    friends = user_profile.friends.all()
    
    context = {'user': user_profile, 'friends': friends}
    return render(request, 'chatapp/index.html', context)


def detail(request,pk):
    friend = Friend.objects.get(profile_id=pk)
    context = {"friend":friend}
    return render(request, 'chatapp/detail.html', context)


def friend_view(request, pk):
    friend = Friend.objects.get(id=pk)
    return render(request, 'chatapp/detail.html', {'friend': friend})


from django.shortcuts import render, get_object_or_404, redirect


def chat_view(request, pk):
    friend = get_object_or_404(Friend, id=pk)  
    chat_room, created = ChatRoom.objects.get_or_create(
        members__in=[request.user, friend.profile.user], 
        is_group=False
    )  
    messages = Message.objects.filter(chat_room=chat_room).order_by('created_at')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Message.objects.create(chat_room=chat_room, sender=request.user, content=content)
            return redirect('chatapp:chat_view', pk=pk)
    else:
        form = MessageForm()

    return render(request, 'chatapp/chat.html', {'friend': friend, 'chat_room': chat_room, 'messages': messages, 'form': form})
