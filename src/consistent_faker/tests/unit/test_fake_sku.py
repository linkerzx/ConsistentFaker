"""
Unit tests for Fake SKu

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
from consistent_faker.classes import FakeSku
from consistent_faker.utils import is_json


class TestFakeSku(unittest.TestCase):
    """
    Unit tests for Fake SKu
    """

    def setUp(self):
        self._fake_sku = FakeSku()

    @property
    def fake_sku(self):
        """FakeSku"""
        return self._fake_sku

    def test_ean_type(self):
        """
        Test that the ean is a string
        """
        self.assertIs(type(self.fake_sku.ean), str)

    def test_title_type(self):
        """
        Test that the title is a string
        """
        self.assertIs(type(self.fake_sku.title), str)

    def test_description_type(self):
        """
        Test that the description is a string
        """
        self.assertIs(type(self.fake_sku.description), str)

    def test_to_dict_type(self):
        """
        Test that to_dict() returns a dict
        """
        self.assertIs(type(self.fake_sku.to_dict()), dict)

    def test_to_json_type(self):
        """
        Test that to_json returns a valid json
        """
        my_json = self.fake_sku.to_json()
        self.assertIs(type(my_json), str)
        self.assertIs(is_json(my_json), True)
