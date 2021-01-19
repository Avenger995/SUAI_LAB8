import unittest
from Lab8 import check_country
from Lab8 import check_third


class NameTestCase(unittest.TestCase):
    # Тесты для Lab8#

    def test_first(self):
        # Тест на страну -#
        mas_country = ['AUS', 'AUT', 'BEL', 'CAN', 'CZE', 'DNK', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL',
                        'ITA','JPN', 'KOR', 'LUX', 'MEX', 'NLD', 'NZL', 'NOR', 'POL', 'PRT', 'SVK', 'ESP', 'SWE', 'CHE',
                        'TUR', 'GBR', 'USA', 'OEU', 'CHL', 'EST', 'ISR', 'SVN', 'OECD']
        result = check_country('', mas_country)
        self.assertEqual(result, 1)

    def test_second(self):
        # Тест на страну +
        mas_country = ['AUS', 'AUT', 'BEL', 'CAN', 'CZE', 'DNK', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL',
                       'ITA', 'JPN', 'KOR', 'LUX', 'MEX', 'NLD', 'NZL', 'NOR', 'POL', 'PRT', 'SVK', 'ESP', 'SWE', 'CHE',
                       'TUR', 'GBR', 'USA', 'OEU', 'CHL', 'EST', 'ISR', 'SVN', 'OECD']
        result = check_country('AUS', mas_country)
        self.assertEqual(result, 0)

    def test_third(self):
        # Тест на пустой ввод
        result = check_third('')
        self.assertEqual(result, 'Ничего не введено. Попробуйте ввести значение снова.')

    def test_fourth(self):
        # Тест на сивол
        result = check_third('a')
        self.assertEqual(result, 'Введен символ или несколько значений. Попробуйте ввести значение снова.')

    def test_fifth(self):
       # Тест на отрицательнрое значение
       result = check_third('-2')
       self.assertEqual(result, 'Введено отрицательное значение. Попробуйте ввести значение снова.')

    def test_sixth(self):
        # Тест на лимит
        result = check_third('37')
        self.assertEqual(result, 'Превышен лимит. Попробуйте ввести значение снова.')

    def test_seventh(self):
        # Тест на вещественное число
        result = check_third('5.7')
        self.assertEqual(result, 'Введено вещественное число. Попробуйте ввести значение снова.')

if __name__ == "__name__":
    unittest.main()
