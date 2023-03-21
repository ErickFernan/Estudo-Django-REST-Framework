import requests
import jsonpath


avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados1 = avaliacoes.json()['results']
# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

# print(resultados1)
# print(resultados)

# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeira)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

# nota_dada = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
# print(nota_dada)

# Todos os nomes das pessoas que avaliaram o curso
nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)
