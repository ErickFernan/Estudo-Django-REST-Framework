import requests

header = {'Authorization': 'Token 5dcb2f0ca2a035407fe77d38e84807c2ef2f9977'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "Novo curso de scrum 3",
    "url": "http://scrummmmmmmmmmmmm.com.br"
}

# Buscando curso com id 4
# curso = requests.get(url=f'{url_base_cursos}4/', headers=header)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}4/', headers=header, data=curso_atualizado)


# Testando cóodigo de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']

