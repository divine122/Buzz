from django.urls import path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path('', views.index , name='index'),
    path('messages/<str:pk>', views.detail, name='detail'),
    path('<str:friend_name>/', views.chat_with_friend, name='message_with_friend'),

]