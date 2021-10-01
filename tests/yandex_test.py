import unittest
from yandex import YandexFolder


class YandexTest(unittest.TestCase):

    def test_1_folder_status(self):
        folder = YandexFolder()
        self.assertEqual(folder.new_folder().status_code, 201)

    def test_2_folder_info(self):
        folder = YandexFolder()
        response = folder.folder_info()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'test')

    def test_3_folder_exists(self):
        folder = YandexFolder()
        self.assertNotEqual(folder.new_folder().status_code, 201)

