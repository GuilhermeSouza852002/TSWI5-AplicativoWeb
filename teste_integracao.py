import unittest
from unittest import mock
from app import app


class AppIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_register_integration(self):
        with mock.patch('app.db') as mock_db:
            mock_db.insert_user.return_value = True
            response = self.app.post('/', data=dict(username='john', password='password'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            mock_db.insert_user.assert_called_once_with('john', 'password')

    def test_edit_user_integration(self):
        with mock.patch('app.db') as mock_db:
            mock_db.update_user.return_value = True
            response = self.app.post('/users/edit/john', data=dict(username='johnny', password='newpassword'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            mock_db.update_user.assert_called_once_with('john', 'johnny', 'newpassword')

    def test_delete_user_integration(self):
        with mock.patch('app.db') as mock_db:
            mock_db.delete_user.return_value = True
            response = self.app.post('/users/delete/john', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            mock_db.delete_user.assert_called_once_with('john')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
