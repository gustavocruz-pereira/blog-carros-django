from urllib import request
from django.shortcuts import render
from .models import Comentario
from .forms import ComentarioForm
from django.shortcuts import HttpResponseRedirect


def addcoment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            data = Comentario()
            data.nome_comentario = form.cleaned_data['nome_comentario']
            data.comentario = form.cleaned_data['comentario']
            data.post_comentario = id
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)