import requests

header = {'Authorization': 'Token 5dcb2f0ca2a035407fe77d38e84807c2ef2f9977'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}4/', headers=header)

# Testando o código HTTP 204
assert resultado.status_code == 204

# Testando se o tamanho do contéudo retornado é 0
assert len(resultado.text) == 0
