from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User


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
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            return redirect('/usuarios/cadastro')

        try:
            # TODO: validar se o username não existe
            user = User.objects.create_user(
                username=username,
                password=senha,
                email=email,
                first_name=primeiro_nome,
                last_name=ultimo_nome
            )
        except:
            return redirect('/usuarios/cadastro')

        user.save()

        return redirect('/usuarios/cadastro')
