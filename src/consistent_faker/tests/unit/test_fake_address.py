"""
Unit tests for Fake Address

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
from consistent_faker.classes import FakeAddress
from consistent_faker.utils import is_json


class TestFakeAddress(unittest.TestCase):
    """
    Unit tests for Fake Address
    """

    def setUp(self):
        self._fake_address = FakeAddress()

    @property
    def fake_address(self):
        """FakeAddress"""
        return self._fake_address

    def test_address_type(self):
        """
        Test that the address_type is a numpy.str_
        """
        self.assertIs(type(self.fake_address.address_type), numpy.str_)

    def test_first_name_type(self):
        """
        Test that the first_name is a string
        """
        self.assertIs(type(self.fake_address.first_name), str)

    def test_last_name_type(self):
        """
        Test that the last_name is a string
        """
        self.assertIs(type(self.fake_address.last_name), str)

    def test_address1_type(self):
        """
        Test that the address1 is a string
        """
        self.assertIs(type(self.fake_address.address1), str)

    def test_address2_type(self):
        """
        Test that the address2 is a string
        """
        self.assertIs(type(self.fake_address.address2), str)

    def test_city_type(self):
        """
        Test that the city is a string
        """
        self.assertIs(type(self.fake_address.city), str)

    def test_province_type(self):
        """
        Test that the city is a string # still in todo
        """
        # self.assertIs(type(self.fake_address.province), str)

    def test_country_type(self):
        """
        Test that the country is a string
        """
        self.assertIs(type(self.fake_address.country), str)

    def test_country_code_type(self):
        """
        Test that the country code is a string
        """
        self.assertIs(type(self.fake_address.country_code), str)

    def test_to_dict_type(self):
        """
        Test that to_dict returns a dict
        """
        self.assertIs(type(self.fake_address.to_dict()), dict)

    def test_to_json_type(self):
        """
        Test that to_json returns a valid json
        """
        my_json = self.fake_address.to_json()
        self.assertIs(type(my_json), str)
        self.assertIs(is_json(my_json), True)
