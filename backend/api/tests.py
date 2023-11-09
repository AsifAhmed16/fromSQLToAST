from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import SQLToAST


class SQLToASTViewSetTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_sql_to_ast(self):
        url = '/api/sqltoast/'
        data = {
            'original_query': 'SELECT a, b FROM test WHERE a = 5;'
        }

        modified_query = "SELECT ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb, 3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d FROM test WHERE ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb = 5;"

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertIn('original_query', response.data)
        self.assertIn('ast', response.data)
        self.assertIn('modified_query', response.data)
        self.assertIn('hashed_values', response.data)

        # Testing, if the object is saved in the database
        created_object = SQLToAST.objects.get(pk=response.data['id'])
        self.assertEqual(created_object.original_query, data['original_query'])
        self.assertEqual(created_object.modified_query, modified_query)


class ASTToSQLViewSetTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        url = '/api/sqltoast/'
        data = {
            'original_query': 'SELECT a, b FROM test WHERE a = 5;'
        }
        self.response = self.client.post(url, data, format='json')

    def test_recreate_sql_from_ast(self):
        # Check recreate of sql from ast
        url = '/api/asttosql/'
        data = {
            'ast_query': 'SELECT ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb, 3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d FROM test WHERE ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb = 5;'
        }
        original_query = "SELECT a, b FROM test WHERE a = 5;"
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, original_query)
