import unittest
from module_03_ci_culture_beginning.homework.hw4.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Vaino Piiranen', 2005)

    def test_get_age(self):
        self.assertEqual(self.person.get_age(), 19)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), 'Vaino Piiranen')

    def test_set_name(self):
        self.person.set_name("Lisa Doolitle")
        self.assertEqual(self.person.get_name(), "Lisa Doolitle")

    def test_set_address(self):
        self.person.set_address('123 Nevsky Prospekt')
        self.assertEqual(self.person.get_address(), '123 Nevsky Prospekt')

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), "")

    def test_is_homeless(self):
        self.assertTrue(self.person.is_homeless())
        self.person.set_address('123 Nevsky Prospekt')
        self.assertFalse(self.person.is_homeless())




