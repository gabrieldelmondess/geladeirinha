from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username= request.POST.get('username')
        email= request.POST.get('email')
        senha= request.POST.get('senha')
        
    user = User.objects.filter(username=username).first()
    
    if user:
        return HttpResponse('USUÁRIO JA CADASTRADO')
    
    user = User.objects.create_user(username=username, email=email, password=senha)
    user.save()
    return HttpResponse("USUARIO CADASTRADO COM SUCESSO!")

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        
        if user:
            login(request,user)
            return HttpResponse('LOGADO!')
        else:
            return HttpResponse('EMAIL OU SENHA INVÁLIDOS!')

def my_logout(request):
    logout(request)
    return HttpResponse('Logout Realizado.')
        
@login_required(login_url="/auth/login/")
def plataforma(request):
        return render(request, 'logado.html')


# Create your views here.
