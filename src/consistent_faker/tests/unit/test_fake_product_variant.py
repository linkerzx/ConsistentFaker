"""
Unit tests for Fake Product Variant
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
