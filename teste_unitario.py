import unittest
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_register(self):
        response = self.app.post('/', data=dict(username='john', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode('utf-8')
        self.assertIn('Lista de Usuários Cadastrados', response_text)
        self.assertIn('john', response_text)

    def test_edit_user(self):
        response = self.app.post('/users/edit/john', data=dict(username='johnny', password='newpassword'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode('utf-8')
        self.assertIn('Lista de Usuários Cadastrados', response_text)
        self.assertIn('johnny', response_text)

    def test_delete_user(self):
        response = self.app.post('/users/delete/john', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode('utf-8')
        self.assertNotIn('john', response_text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
