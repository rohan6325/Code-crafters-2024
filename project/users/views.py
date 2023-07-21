from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method =='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            Username= form.cleaned_data.get('username')
            messages.success(request,f'Your Account is created for username :{Username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})
@login_required
def profile(request):
    return render(request, 'profile.html')