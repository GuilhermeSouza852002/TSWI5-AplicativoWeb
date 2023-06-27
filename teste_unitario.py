#Importação
import unittest
from app import app


class AppTestCase(unittest.TestCase):
    
    #permite enviar solicitações HTTP simuladas para o aplicativo durante os testes
    def setUp(self):
        self.app = app.test_client()

    # envia uma solicitação POST para a rota '/', simulando o envio de um formulário com dados de usuário
    def test_register(self):
        response = self.app.post('/', data=dict(username='john', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)                     #verifica se a resposta tem um código de status 200
        response_text = response.data.decode('utf-8')
        self.assertIn('Lista de Usuários Cadastrados', response_text)   #se a página contém a frase 'Lista de Usuários Cadastrados'
        self.assertIn('john', response_text)                            #se a página contém o nome de usuário 'john'

    # envia uma solicitação POST para a rota '/users/edit/<username>', simulando a edição de um formulário com dados de usuário
    def test_edit_user(self):
        response = self.app.post('/users/edit/john', data=dict(username='johnny', password='newpassword'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode('utf-8')
        self.assertIn('Lista de Usuários Cadastrados', response_text)
        self.assertIn('johnny', response_text)

    # envia uma solicitação POST para a rota '/users/delete/<username>', simulando a exclusão de um formulário com dados de usuário
    def test_delete_user(self):
        response = self.app.post('/users/delete/john', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode('utf-8')
        self.assertNotIn('john', response_text)

    #realizar limpezas ou fechar conexões após os testes
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
