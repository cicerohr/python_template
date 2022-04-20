from unittest import TestCase

from tools.emails import is_valid, is_same


class TestEmails(TestCase):
    def test_are_valid_username_and_domain_and_tld(self):
        self.assertEqual(is_valid('username@domain.tld'), True)

    def test_is_valid_username_and_domain_and_tld_and_cctld(self):
        self.assertEqual(is_valid('username@domain.tld.io'), True)

    def test_is_valid_domain_with_dot_and_number(self):
        self.assertEqual(is_valid('username@domain.12345.tld.io'), True)

    def test_is_valid_only_username(self):
        self.assertEqual(is_valid('username'), False)

    def test_is_valid_only_at_and__domain(self):
        self.assertEqual(is_valid('@domain.tld'), False)

    def test_is_valid_only_at(self):
        self.assertEqual(is_valid('@'), False)

    def test_is_valid_only_username_domain(self):
        self.assertEqual(is_valid('username@domain'), False)

    def test_is_valid_only_username_domain_and_dot(self):
        self.assertEqual(is_valid('username@domain.'), False)

    def test_is_valid_only_username_domain_and_dot_and_number(self):
        self.assertEqual(is_valid('username@domain.123'), False)

    def test_is_same(self):
        self.assertEqual(is_same('username@domain.tld', 'username@domain.tld'), True)

    def test_is_same_different_domain(self):
        self.assertEqual(is_same('username@domain.tld', 'username@domain1.tld'), False)

    def test_is_same_different_username(self):
        self.assertEqual(is_same('username.doe@domain.tld', 'username@domain.tld'), False)

    def test_is_same_but_wrong_format(self):
        self.assertEqual(is_same('username@domain', 'username@domain'), False)
