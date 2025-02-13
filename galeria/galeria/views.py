from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    # dados = {
    #     1: {"nome": "Nebulosa de Carina", "legenda": "webbtelecop.org / NASA / James Webb"},
    #     2: {"nome": "Galáxia NGC 1079", "legenda": "nasa.org / NASA / Hubble"},
        
    # }
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})