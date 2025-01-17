from django.urls import path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path('', views.index , name='index'),
    path('friend/<int:pk>/', views.detail, name='detail'),
    path('chat/<int:pk>/', views.chat_view, name='chat_view'),
    

]