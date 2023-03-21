import requests

header = {'Authorization': 'Token 5dcb2f0ca2a035407fe77d38e84807c2ef2f9977'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


novo_curso = {
    "titulo": "Teste POST",
    "url": "http://testepost.com.br"
}

resultado = requests.post(url=url_base_cursos, headers=header, data=novo_curso)

# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']