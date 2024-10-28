from django.shortcuts import render
import requests

def buscar_filmes(request):
  filme = None
  erro = None
  if request.method == 'POST':
    titulo = request.POST.get('titulo')
    try:
      response = requests.get(f'http://www.omdbapi.com/?apikey=97ed8a41&t={titulo}&type=movie')
      filme = response.json()
      if filme['Response'] == 'False':
        erro = 'Filme não encontrado!'
    except:
      erro = 'Erro: falha na conexão'
  return render (request, 'index.html', {'filme': filme, 'erro': erro})  
    
def index(request):
    return render(request, 'index.html')