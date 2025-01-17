from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ChatRoom(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    is_group = models.BooleanField(default=False)
    members = models.ManyToManyField(User, related_name='chat_room')
    created_at = models.DateTimeField(auto_now_add=True)
    last_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name or f"Chat Room {self.id}"
    
class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'messages')
    content = models.TextField(blank=True)
    media = models.FileField(upload_to= 'chat_media/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read_by = models.ManyToManyField(User, blank=True, related_name='read_messages')

    def __str__(self):
        return f"Message from {self.sender} in {self.chat_room}"


class Notification(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)    
    status = models.CharField(max_length=300,blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name='my_friends')
    

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

class Friend(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='friend')    

    def __str__(self):
        return f"Friend of {self.profile.user.username}"