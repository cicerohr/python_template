from unittest import TestCase

from tools.currency_converter import CurrencyConverter


class TestCurrencyConverter(TestCase):
    def test_convert_currency(self):
        converter = CurrencyConverter('EUR', 'BRL', 2)
        self.assertEqual(converter.convert(), 10.123592)

    def test_convert_currency_with_invalid_currency(self):
        converter = CurrencyConverter('US', 'EUR', 1)
        self.assertEqual(converter.convert(), False)

    def test_convert_currency_with_invalid_amount(self):
        converter = CurrencyConverter('USD', 'EUR', 'a')
        self.assertEqual(converter.convert(), False)

    def test_convert_currency_with_invalid_currency_and_amount(self):
        converter = CurrencyConverter('US', 'EU', 'a')
        self.assertEqual(converter.convert(), False)
