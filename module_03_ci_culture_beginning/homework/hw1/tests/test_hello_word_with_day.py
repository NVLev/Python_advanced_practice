import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from freezegun import freeze_time
from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import app, GREETINGS


#
class TestHelloWorldDateApp(unittest.TestCase):
    """
    Tarkistetaan, onko viikonpäivä palautettu oikein
    Käyttään freeze_time-metodia freezegun kirjastosta
    """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_correct_weekday(self):
        for i in range(7):
            # print(i)
            day = timedelta(days=i)
            data = datetime.now() + day
            with freeze_time(data) as frozen_datetime:
                username = 'username'
                weekday = data.weekday()
                response = self.app.get(self.base_url + username)
                today = GREETINGS[weekday]
                response_text = response.data.decode()
                self.assertTrue(today in response_text)


if __name__ == '__main__':
    unittest.main()
