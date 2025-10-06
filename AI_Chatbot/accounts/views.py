from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created sucessfully for {username}!')
            login(request,user)
            return redirect('home')
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    messages.error(request,f'{error}')
    else:
        form=RegistrationForm()
    return render(request,'accounts/register.html',{'form':form}) 


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'Welcome back {username}!')
                return redirect('home')
        else:
                messages.error(request,'Invalid username or password')
    else:
        form=LoginForm()
    return render(request,'accounts/login.html',{'form':form})


def logoutview(request):
    logout(request)
    messages.success(request,'You have been logged out successfully')
    return redirect('login')

def home_view(request):
    return render(request,'home.html',{})