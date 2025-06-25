from django.shortcuts import redirect, render

from usuarios.forms import CadastroForms, LoginForms

from django.contrib.auth.models import User

from django.contrib import auth

# Create your views here.

def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
        
        user = auth.authenticate(
            request,
            username=nome, 
            password=senha
        )
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form['senha'].value() != form['confirmar_senha'].value():
                return redirect('cadastro')
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha'].value()
            
            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
            
            user = User.objects.create_user(
                username=nome, 
                email=email, 
                password=senha
            )
            user.save()
            return redirect('login')
            
    return render(request, 'usuarios/cadastro.html', {'form': form})