import unittest
from module_03_ci_culture_beginning.homework.hw2.decrypt import decrypt


class TestDecrypt(unittest.TestCase):
    """
    Luokka testejä, joilla tarkistetaan dekooderin toiminta
    """

    def setUp(self):
        self.response_list1 = ['абра-кадабра.', 'абраа..-кадабра', 'абраа..-.кадабра', 'абра--..кадабра',
                               'абрау...-кадабра']
        self.response_list2 = ['.', 'абра........', '1.......................']

    def test_decrypt_result1(self):
        for el in self.response_list1:
            expected_result = 'абра-кадабра'
            actual_result = decrypt(el)
            with self.subTest(el=el):
                self.assertEqual(expected_result, actual_result)

    def test_decrypt_result2(self):
        for el in self.response_list2:
            expected_result = ''
            actual_result = decrypt(el)
            with self.subTest(el=el):
                self.assertEqual(expected_result, actual_result)

    def test_decrypt_unattached1(self):
        expected_result = 'абр......a.'
        actual_result = decrypt('a')
        self.assertEqual(expected_result, actual_result)

    def test_decrypt_unattached2(self):
        expected_result = 'self.assertEqual(expected_result, actual_result)'
        actual_result = decrypt('23')
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
