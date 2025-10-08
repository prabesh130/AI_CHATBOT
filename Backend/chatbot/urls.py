from django.urls import path 
from . import views


urlpatterns=[
    path('chatpage/',views.chat_view,name='chatpage'),


]