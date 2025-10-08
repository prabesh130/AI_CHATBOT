from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def chat_view(request):
    return render(request,'chatbot/chatpage.html',{})

# Create your views here.
