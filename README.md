# Django Space 🪐

Bem-vindo ao **Django Space**, um projeto de estudos criado do zero para aprender os fundamentos do framework **Django** de forma prática e estruturada. Este repositório é ideal para iniciantes que desejam dominar os conceitos básicos de desenvolvimento web com Django.

---

## 📖 Sobre o Projeto

O **Django Space** é um projeto de aprendizado focado em explorar os pilares do Django, como modelos, views, templates, URLs e administração. Ele foi desenhado para ser um ponto de partida para quem está começando a estudar desenvolvimento web com Python e quer construir uma base sólida.

### Objetivos

- Configurar um projeto Django do zero.
- Entender o funcionamento de **modelos**, **views** e **templates**.
- Configurar rotas (URLs) e a interface de administração.
- Explorar o **ORM** do Django para manipulação de banco de dados.
- Aplicar boas práticas de organização e desenvolvimento.

---

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍: Linguagem principal.
- **Django** 🌐: Framework web.
- **SQLite** 🗄️: Banco de dados padrão para desenvolvimento.
- **Virtualenv** 📦: Para isolamento de dependências.

---

## 📋 Pré-requisitos

Para rodar o projeto, você precisa ter instalado:

- Python 3.8+
- pip
- Git
- **virtualenv** (para gerenciar ambientes virtuais)

---

## 🚀 Como Configurar

Siga os passos abaixo para configurar o projeto localmente usando **virtualenv**:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/django-space.git
   cd django-space
   ```

2. **Crie e ative um ambiente virtual com virtualenv**:

   ```bash
   virtualenv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

   *Nota*: Após ativar o ambiente, você verá `(venv)` no terminal, indicando que está no ambiente virtual.

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações**:

   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor**:

   ```bash
   python manage.py runserver
   ```

6. Abra o navegador e acesse:\
   🌍 `http://localhost:8000`

---

## 📂 Estrutura do Projeto

```plaintext
django-space/
├── manage.py           # Script principal do Django
├── setup/             # Configurações do projeto
│   ├── settings.py    # Configurações gerais
│   ├── urls.py        # Rotas do projeto
│   └── wsgi.py        # Configuração WSGI
├── app/               # (A ser criado) Apps do projeto
├── venv/              # Ambiente virtual (não versionado no Git)
├── requirements.txt   # Dependências
└── README.md          # Este arquivo
```

---

## 🔮 Próximos Passos

O projeto será expandido com os seguintes tópicos:

- Criação de **modelos** e relacionamentos no banco de dados.
- Desenvolvimento de **views** baseadas em classes e funções.
- Configuração de **formulários** e validação de dados.
- Integração com **Bootstrap** para estilização.
- Implementação de **autenticação** e **autorização**.

---

## 🤝 Contribuições

Este é um projeto de estudos, mas ideias e melhorias são sempre bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`.
3. Commit suas mudanças: `git commit -m "Adiciona minha feature"`.
4. Envie para o repositório: `git push origin minha-feature`.
5. Abra um **Pull Request**.

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
