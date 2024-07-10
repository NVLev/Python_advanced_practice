import unittest
from module_03_ci_culture_beginning.homework.hw3.accounting import app, storage, add


class TestAccountingApp(unittest.TestCase):
    """
    Luokka testejä, joilla tarkistetaan "Talouden kirjanpito" -sovelluksen suorituskyky.
    - Täyttää storage sanakirjan alkuperäisillä tiedoilla.
    - Tarkistaa, että päätepiste /add/ on käynnissä.
    - Tarkistaa, että molemmat päätepisteet /calculate/ toimivat.
    - Tarkistaa, että päätepiste /add/ voi hyväksyä vain päivämäärän muodossa VVVVVVKKPP.
    - Tarkistetaan, että päätepiste /calculate/ toimii, jos tallennuksessa ei ole mitään.
    """
    storage = {}

    @classmethod
    def setUpClass(cls):
        cls.base_url_add = '/add/'
        cls.base_url_calculate = '/calculate/'
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.storage.update({
            '2024': {
                '02': 300
            }
        })

    def test_add_endpoint(self):
        date: int = 20240210
        number: int = 300
        response = self.app.get(self.base_url_add + str(date) + '/' + str(number))
        self.assertEqual(response.status_code, 200)

    def test_correct_endpoint_add(self):
        date: int = 20240210
        number: int = 300
        response = self.app.get(self.base_url_add + str(date) + '/' + str(number))
        self.assertEqual(
            response.request.path, self.base_url_add + str(date) + '/' + str(number)
        )

    def test_calculate_endpoint_works(self):
        vuosi: int = 2024
        response = self.app.get(self.base_url_calculate + str(vuosi))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.path, f'/calculate/{vuosi}')

    def test_correct_endpoint_calculate_month(self):
        vuosi: int = 2024
        kuukausi: int = 2
        response = self.app.get(self.base_url_calculate + str(vuosi) + '/' + str(kuukausi))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.path, f'/calculate/{vuosi}/{kuukausi}')

    def test_add_accept_date(self):
        with self.assertRaises(TypeError):
            add('ymd')

    def test_calculate_year_empty_storage(self):
        storage.clear()
        vuosi: int = 2024
        response = self.app.get(self.base_url_calculate + str(vuosi))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Tänä vuonna ei ole vielä ollut menoja')

    def test_calculate_month_empty_storage(self):
        storage.clear()
        vuosi: int = 2024
        kuu: int = 2
        response = self.app.get(self.base_url_calculate + str(vuosi) + '/' + str(kuu))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Tässä kuukaudessa ei ole vielä ollut menoja')


if __name__ == '__main__':
    unittest.main()
