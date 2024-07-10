import unittest
from . import wtf_beginning
from wtf_beginning import app, register


class TestWrfBeginning(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/register'

    def test_name_filled(self):
        response = register()
