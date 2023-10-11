from django.shortcuts import redirect, render
from django.contrib.messages import constants
from django.contrib import messages
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def cadastro(req):
    if req.method == 'GET':
        return render(req, 'cadastro.html')

    elif req.method == 'POST':
        primeiro_nome = req.POST.get('primeiro_nome')
        ultimo_nome = req.POST.get('ultimo_nome')
        username = req.POST.get('username')
        senha = req.POST.get('senha')
        email = req.POST.get('email')
        confirmar_senha = req.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(req, constants.ERROR,
                                 'As senhas não são iguais.')

        if len(senha) < 6:
            messages.add_message(req, constants.ERROR,
                                 'A senha precisa ter 7 ou mais digitos.')

        if User.objects.filter(username=username).exists():
            messages.add_message(req, constants.ERROR,
                                 'Username já cadastrado.')
            return redirect('/usuarios/cadastro')

        try:
            user = User.objects.create_user(
                username=username,
                password=senha,
                email=email,
                first_name=primeiro_nome,
                last_name=ultimo_nome
            )

            user.save()

            messages.add_message(req, constants.SUCCESS,
                                 'Usuário cadastrado com sucesso.')

        except:
            messages.add_message(req, constants.ERROR,
                                 'Erro ao cadastrar usuário.')
            return redirect('/usuarios/cadastro')

        return redirect('/usuarios/cadastro')


def logar(req):
    if req.method == 'GET':
        return render(req, 'login.html')

    elif req.method == 'POST':
        username = req.POST.get('username')
        senha = req.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(req, user)
            return redirect('/')
        else:
            messages.add_message(req, constants.ERROR,
                                 'Usuário ou senha inválidos.')
            return redirect('/usuarios/login')
