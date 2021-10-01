import unittest
from unittest.mock import patch
from app import show_document_info, add_new_doc, delete_doc, get_doc_shelf, documents


@patch('builtins.input', lambda *args: 'test')
class AppTest(unittest.TestCase):

    def test_document_info(self):
        for doc in documents:
            self.assertIsInstance(show_document_info(doc), str)

    def test_document_add(self):
        self.assertEqual(add_new_doc(), 'test')
        self.assertEqual(get_doc_shelf(), 'test')

    def test_document_delete(self):
        self.assertEqual(delete_doc(), ('test', True))

