# -*- coding: utf-8 -*-
r"""currency_converter.py in: 2022-04-19.

Python version: 3.10.0

Currency converter.
- The class uses 'The Currency Converter API' v7 to convert currencies.
(https://www.currencyconverterapi.com/docs)
- The user must enter the ISO 4217 code of the source currency and the
target currency. A numeric value of the amount to be converted.
- The class checks whether the entries are valid.
- The class returns the converted amount.
"""
import requests

from logs.loguru_conf import logger

# TODO: store api key on an encrypted server.
API_KEY = '5f017427a45873191a79'


class CurrencyConverter:
    """Currency converter class."""

    def __init__(
            self, source_currency: str, target_currency: str, amount: float
    ) -> None:
        """Initialize the class."""
        self.source_currency = source_currency
        self.target_currency = target_currency
        self.amount = amount
        self.api_domain = 'https://free.currconv.com'
        self.api_version = '/api/v7'
        self.__api_key = f'apiKey={API_KEY}'
        self.query_converter = (
            f'/convert?q={source_currency}_{target_currency}&compact=ultra&'
        )
        self.response = None
        self.converted_amount = None
        logger.debug(f'CurrencyConverter.__init__: {self.__repr__()}')

    def __str__(self):
        """Return a string representation of the class."""
        return (
            f'CurrencyConverter({self.source_currency}, '
            f'{self.target_currency}, {self.amount}) '
            f'-> {self.converted_amount}'
        )

    def __repr__(self):
        """Return a string representation of the class."""
        return (
            f'CurrencyConverter({self.source_currency}, '
            f'{self.target_currency}, {self.amount}) '
            f'-> {self.converted_amount}'
        )

    def check_valid_currency(self) -> bool:
        """Check if the currency is valid.

        :return: True if the currency is valid, False otherwise.
        :rtype: bool
        """
        logger.debug(
            f'CurrencyConverter.check_valid_currency: {self.__repr__()}'
        )
        split_key = list(self.response.json().keys())[0].split('_')
        if self.source_currency not in split_key[0]:
            logger.error(
                f'CurrencyConverter.check_valid_currency: '
                f'{self.source_currency} is not a valid currency.'
            )
            return False
        if self.target_currency not in split_key[1]:
            logger.error(
                f'CurrencyConverter.check_valid_currency: '
                f'{self.target_currency} is not a valid currency.'
            )
            return False
        return True

    def check_valid_amount(self) -> bool:
        """Check if the amount is valid.

        Must be a positive number and not zero.
        Must be different from characters.

        :return: True if the amount is valid, False otherwise.
        :rtype: bool
        """
        logger.debug(
            f'CurrencyConverter.check_valid_amount: {self.__repr__()}'
        )
        try:
            float(self.amount)
        except ValueError:
            logger.error(
                f'CurrencyConverter.check_valid_amount: '
                f'{self.amount} is not a valid amount.'
            )
            return False
        if self.amount <= 0:
            logger.error(
                f'CurrencyConverter.check_valid_amount: '
                f'{self.amount} is not a valid amount.'
            )
            return False
        return True

    def get_data(self) -> dict | bool:
        """Get the data from the API.

        :return: data from the API.
        :rtype: dict or False
        """
        url = (
            f'{self.api_domain}{self.api_version}'
            f'{self.query_converter}{self.__api_key}'
        )
        self.response = requests.get(url)
        if self.response.status_code != 200:
            logger.error(
                f'CurrencyConverter.get_data: '
                f'{self.response.status_code} {self.response.reason}'
            )
            return False
        logger.debug(f'CurrencyConverter.get_data: {self.response.json()}')
        return self.response.json()

    def convert(self) -> float | bool:
        """Convert the currency.

        :return: converted amount.
        :rtype: float or False
        """
        data = self.get_data()
        logger.debug(f'CurrencyConverter.convert: {data}')
        if not data:
            logger.error(
                f'CurrencyConverter.convert: '
                f'{self.__repr__()} is not a valid data.'
            )
            return False
        if not self.check_valid_currency():
            logger.error(
                f'CurrencyConverter.convert: '
                f'{self.__repr__()} is not a valid currency.'
            )
            return False
        if not self.check_valid_amount():
            logger.error(
                f'CurrencyConverter.convert: '
                f'{self.__repr__()} is not a valid amount.'
            )
            return False
        try:
            self.converted_amount = (
                    self.amount
                    * data[f'{self.source_currency}_{self.target_currency}']
            )
        except KeyError:
            logger.error(
                f'CurrencyConverter.convert: '
                f'{self.source_currency}_{self.target_currency} is not a valid'
                f' currency pair.'
            )
            return False
        logger.debug(f'CurrencyConverter.convert: {self.converted_amount}')
        return self.converted_amount


def main():
    """Main function."""
    source_currency = input('Enter the source currency: ').strip().upper()[:3]
    target_currency = input('Enter the target currency: ').strip().upper()[:3]
    amount = float(input('Enter the amount to be converted: '))
    converter = CurrencyConverter(source_currency, target_currency, amount)
    converted_amount = converter.convert()
    if converted_amount:
        print(f'The converted amount is {converted_amount}.')
    else:
        print('The conversion failed.')


if __name__ == '__main__':
    logger.debug('main: start')
    main()
    logger.debug('main: end')
