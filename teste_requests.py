import requests


# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')


# Acessando o código de status HTTP
# print(avaliacoes.status_code)


# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))


# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])


# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])


# Acessando os resultados desta página
# print(avaliacoes.json()['results'])


# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])


# Acessando o ultimo elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])


# Acessando somento o nome da pessoa que fez a ultim avaliacao
# print(avaliacoes.json()['results'][0]['nome'])


# GET Avaliacao

avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')

print(avaliacao.json())


# GET Cursos

headers = {'Authorization': 'Token 5dcb2f0ca2a035407fe77d38e84807c2ef2f9977'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos.json())
print(cursos.status_code)
