"""
Unit Tests for Fake Email

Copyright (c) 2019 Julien Kervizic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import unittest
import numpy
from consistent_faker.classes import FakeEmail


class TestFakeEmail(unittest.TestCase):
    """
    Unit Tests for Fake Email
    """

    def setUp(self):
        self._fake_email = FakeEmail()

    @property
    def fake_email(self):
        """FakeEmail"""
        return self._fake_email

    def test_first_name_type(self):
        """
        Test that first name is a string
        """
        self.assertIs(type(self.fake_email.first_name), str)

    def test_last_name_type(self):
        """
        Test that last name is a string
        """
        self.assertIs(type(self.fake_email.last_name), str)

    def test_format_type(self):
        """
        Test that the format is a np string
        """
        self.assertIs(type(self.fake_email.format), numpy.str_)

    def test_email_type(self):
        """
        Test that email is a string
        """
        self.assertIs(type(self.fake_email.email), str)

    def test_email_config(self):
        """
        Test that email object can be configured
        """
        my_first_name = "Julien"
        my_last_name = "Kervizic"
        my_email_address = "blabla@bla.com"
        fake_email = FakeEmail(
            first_name=my_first_name,
            last_name=my_last_name,
            email_address=my_email_address,
        )
        self.assertEqual(fake_email.first_name, my_first_name.lower())
        self.assertEqual(fake_email.last_name, my_last_name.lower())
        self.assertEqual(fake_email.email, my_email_address.lower())
