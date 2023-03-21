import requests


class TestCursos:
    headers = {"Authorization": "Token 5dcb2f0ca2a035407fe77d38e84807c2ef2f9977"}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):  # Todo método deve começar com test_ ...
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Teste usando pytest",
            "url": "http://testepytest.org"
        }

        resposta= requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Teste atualização usando pytest",
            "url": "http://testepytest.org/att"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers,  data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Teste atualização2 usando pytest",
            "url": "http://testepytest.org/att2"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):

        resposta = requests.delete(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
