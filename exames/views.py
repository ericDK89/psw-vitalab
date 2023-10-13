import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TiposExames
from django.http import HttpResponse


@login_required
def solicitar_exames(request):
    tipos_exames = TiposExames.objects.all()
    if request.method == 'GET':

        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames, })

    elif request.method == 'POST':
        exame_id = request.POST.getlist('exames')
        solicitacao_exames = TiposExames.objects.filter(id__in=exame_id)

        preco_total = 0
        for i in solicitacao_exames:
            if i.disponivel:
                preco_total += i.preco

        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames,
                                                         'solicitacao_exames': solicitacao_exames,
                                                         'preco_total': preco_total,
                                                         })
