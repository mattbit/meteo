import unittest
from weather import Weather

class TestWeather(unittest.TestCase):
    def test_rainy(self):
        w = Weather()
        self.assertTrue(w.is_rainy())


if __name__ == '__main__':
    unittest.main()