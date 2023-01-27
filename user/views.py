from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def userRegister(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kullanıcı oluşturuldu..")
            return redirect("login")
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def userLogin(request):
    if request.method == "POST":
        kullaniciAdi = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullaniciAdi, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş yapıldı')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış yapıldı')
    return redirect('index')