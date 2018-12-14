from django.shortcuts import render
import operator
#IMPORTANDO O MODEL DE LAWFILE
from .models import LawFile
#IMPORTANDO FUNÇÕES DO POSTGRESQL
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
#IMPORTANDO DEFINIÇÕES DO SEARCHFORM DE FORMS
from .forms import SearchForm

# Create your views here.
########################################################################################################
#OBS: É necessário a criação de uma pasta templates/nome_da_app dentro da pasta da APP para hospedar os#
#arquivos HTML, senão o Django não encontra os templates.                                              #
########################################################################################################
def leis(request):
    lista = {}
    lista['Leis'] = LawFile.objects.all()
    return render(request, 'laws/leis.html', lista)

def decretos(request):
    lista = {}
    lista['Leis'] = LawFile.objects.filter(status='decreto')
    return render(request, 'laws/decretos.html', lista)

def complementar(request):
    lista = {}
    lista['Leis'] = LawFile.objects.filter(status='lei complementar')
    return render(request, 'laws/complementar.html', lista)

def ordinaria(request):
    lista = {}
    lista['Leis'] = LawFile.objects.filter(status='lei ordinária')
    return render(request, 'laws/ordinaria.html', lista)

def organica(request):
    lista = {}
    lista['Leis'] = LawFile.objects.filter(status='lei orgânica')
    return render(request, 'laws/organica.html', lista)

def pesq_lei(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = LawFile.objects.annotate(
                similarity=TrigramSimilarity('number_law', 'date_publish', 'desc_law', query),
            ).filter(similarity__gt=0.3).order_by('-similarity')
    return render(request,
                  'leis/static/pesquisa.html',
                  {'form': form,
                   'query': query,
                   'results': results})