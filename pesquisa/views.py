from django.shortcuts import render
import requests

def buscar_filmes(request):
  filme = None
  erro = None
  if request.method == 'POST':
    titulo = request.POST.get('titulo')
    try:
      response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=53fcec6ea9b78cbac654e8d369e770d4&query={titulo}&language=pt-BR')
      dados = response.json()
      filmes = dados.get('results')
      if not filmes:
        erro = 'Filme não encontrado!'
      else:
        filme = filmes[0]
    except requests.exceptions.HTTPError as http_err:
      erro = f'Erro HTTP: {http_err}'
    except requests.exceptions.RequestException as req_err:
      erro = f'Erro na requisição: {req_err}'
    except Exception as e:
      erro = f'Erro interno: {str(e)}'
  return render (request, 'index.html', {'filme': filme, 'erro': erro})  
    
def index(request):
    return render(request, 'index.html')