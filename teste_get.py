import requests


header = {'Authorization': 'Token 5dcb2f0ca2a035407fe77d38e84807c2ef2f9977'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=header)

# print(resultado.json())

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 6

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Criação de APrI com DJanfo'
