from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    confirmar_senha = forms.CharField(
        label='Confirmação de senha',
        required=True,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha mais uma vez'
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Por favor, digite seu nome sem espaços.')
            else:
                return nome
            
    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')
        
        if senha and confirmar_senha and senha:
            if senha != confirmar_senha:
                raise forms.ValidationError('As senhas não são iguais!')
            else:
                return confirmar_senha