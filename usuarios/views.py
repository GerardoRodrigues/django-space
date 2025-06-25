from django.shortcuts import redirect, render

from usuarios.forms import CadastroForms, LoginForms

from django.contrib.auth.models import User

# Create your views here.

def login(request):
    form = LoginForms()
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