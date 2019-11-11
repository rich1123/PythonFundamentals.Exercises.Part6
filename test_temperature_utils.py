import unittest
import temperature_utils


class TemperatureUtils(unittest.TestCase):

    def test_convert_to_celsius(self):
        self.assertEqual(0, temperature_utils.convert_to_celsius(32))
        self.assertEqual(20, temperature_utils.convert_to_celsius(68))
        self.assertEqual(37.78, temperature_utils.convert_to_celsius(100))
        self.assertEqual(40, temperature_utils.convert_to_celsius(104))

    def test_convert_to_fahrenheit(self):
        self.assertEqual(0, temperature_utils.convert_to_fahrenheit(-17.7778))
        self.assertEqual(32, temperature_utils.convert_to_fahrenheit(0))
        self.assertEqual(212, temperature_utils.convert_to_fahrenheit(100))

    def test_temperature_tuple(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 0.0), (68, 20.0), (100, 37.78), (104, 40.0))
        actual = temperature_utils.temperature_tuple(temps_input, "f")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 0.0), (0, 32.0), (100, 212.0))
        actual = temperature_utils.temperature_tuple(temps_input, "c")
        self.assertEqual(expected, actual)

    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils.temperature_tuple(temps_input, "a"))
