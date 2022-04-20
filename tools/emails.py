"""Tool pack for email.

emails.py in: 2021-12-11.
@author: Cícero

This module exports the following functions:
    -> is_valid - Check if the string is a valid email.
    -> is_same - Check if the two emails are the same.
"""
import doctest
from re import match

# File with the configuration of the loguru logger
from logs.loguru_conf import logger

# public symbols
__all__ = [
    'is_valid',
    'is_same',
]


def is_valid(email: str) -> bool:
    """-> Checks to see if the email address is valid.

    The email address is valid if it has the following format:
    <username>@<domain>.<tld>

    Test:
    >>> is_valid('john.doe@domain.co.uk')
    True
    >>> is_valid('john_doe@domain.br')
    True
    >>> is_valid('john_doe@domain.com.uk')
    True
    >>> is_valid('john_doe@domain.com')
    True
    >>> is_valid('john.doe@domain.com')
    True
    >>> is_valid('jane.doe_23@domain.com.io')
    True
    >>> is_valid('mail')
    False
    >>> is_valid('john.doe@domain')
    False
    >>> is_valid('john.doe@ domain.com')
    False
    >>> is_valid('jane_doe @domain.com')
    False
    >>> is_valid('jane doe@domain.com')
    False
    >>> is_valid('jane.doe@domain.com ')
    False
    >>> is_valid('jane@domain.com.')
    False

    :param email: email to validate
    :return: True if valid, False if not
    :rtype: bool

    """
    logger.debug(f'email: {email}')
    return bool(
        match(r'^[\w.+]+@[\w.-]+\.[a-zA-Z]{2,3}(?:.[a-zA-Z]{2})?$', email))


def is_same(email_1: str, email_2: str) -> bool:
    """-> Checks to see if the two emails are the same.

    The two emails are the same if they have the same username, domain name
    and the same tld.

    Test:
    >>> is_same('jane.doe@domain', 'jane.doe@domain')
    False
    >>> is_same('jane_doe@domain.com', ' jane_doe@domail.com')
    False
    >>> is_same('John_doe@domain.com.uk', 'john_doe@domain.com')
    False
    >>> is_same('jane_doe@domain.com', 'jane_doe@domain.com')
    True

    :param email_1: First email address to compare
    :param email_2: Second email address to compare
    :return: True if the two email addresses are the same, False if not
    :rtype: bool

    """
    logger.debug(f'email_1: {email_1}')
    logger.debug(f'email_2: {email_2}')
    regular_expression = r'^[\w.+]+@[\w.-]+\.[a-zA-Z]{2,3}(?:.[a-zA-Z]{2})?$'
    return bool(
        match(regular_expression, email_1)
        and match(regular_expression, email_2)
        and email_1.split('@')[0] == email_2.split('@')[0]
        and email_1.split('@')[1] == email_2.split('@')[1]
    )


def main():
    """Main function."""
    doctest.testmod()
    list_mails = [
        'jane.doe@domain',
        'jane.doe@domain.',
        'jane.doe@domain.com',
        'john_doe@domain.com.uk',
        'jane.doe@domain.io',
    ]
    for email in list_mails:
        print(
            f'Is {email} valid? {is_valid(email)}; '
            f'Is same? {is_same(email, email)}',
            end='\n\n',
        )


if __name__ == '__main__':
    logger.info('Running')
    main()
    logger.info('Ending')
