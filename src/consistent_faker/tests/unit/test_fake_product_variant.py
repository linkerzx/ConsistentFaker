"""
Unit tests for Fake Product Variant

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
import uuid
import numpy
from consistent_faker.classes import FakeProductVariant
from consistent_faker.classes import FakeSku


class TestFakeProductVariant(unittest.TestCase):
    """
    Unit tests for Fake Product Variant
    """

    def setUp(self):
        self._fake_product_variant = FakeProductVariant()

    @property
    def fake_product_variant(self):
        """FakeProductVariant"""
        return self._fake_product_variant

    def test_sku_type(self):
        """
        Test that the sku is a FakeSku
        """
        self.assertIs(type(self.fake_product_variant.sku), FakeSku)

    def test_uid_type(self):
        """
        Test that the uid is a guid
        """
        self.assertIs(type(self.fake_product_variant.uid), uuid.UUID)

    def test_price_incl_taxes_type(self):
        """
        Test that the price_incl_taxes is a np.float64
        """
        self.assertIs(type(self.fake_product_variant.price_incl_taxes), numpy.float64)

    def test_to_dict_type(self):
        """
        Test that to_dict() returns a dict
        """
        self.assertIs(type(self.fake_product_variant.to_dict()), dict)

    def test_config_price(self):
        """
        Test that price is importable
        """
        my_price_incl_taxes = 4.5
        fpv = FakeProductVariant(price_incl_taxes=my_price_incl_taxes)
        self.assertEqual(fpv.price_incl_taxes, my_price_incl_taxes)
