from django.shortcuts import redirect, render

from usuarios.forms import CadastroForms, LoginForms

from django.contrib.auth.models import User

from django.contrib import auth, messages

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
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect('login')
    
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha'].value()
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já cadastrado!')
                return redirect('cadastro')
            
            user = User.objects.create_user(
                username=nome, 
                email=email, 
                password=senha
            )
            user.save()
            messages.success(request, f'{nome} cadastrado com sucesso!')
            return redirect('login')
            
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')