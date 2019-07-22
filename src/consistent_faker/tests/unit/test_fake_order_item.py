"""
Unit Test for Order Items
"""
import unittest
import uuid
import numpy
from consistent_faker.classes import FakeOrderItem
from consistent_faker.classes import FakeProductVariant
from consistent_faker.utils import is_json


class TestFakeOrderItem(unittest.TestCase):
    """
    Unit Test for Fake Order Items
    """

    def setUp(self):
        self._fake_order_item = FakeOrderItem()

    @property
    def fake_order_item(self):
        """FakeOrderItem"""
        return self._fake_order_item

    def test_uid_type(self):
        """
        Test that the uid is a guid
        """
        self.assertIs(type(self.fake_order_item.uid), uuid.UUID)

    def test_product_prices_incl_taxes_type(self):
        """
        Test that the product prices is a float
        """
        self.assertIs(
            type(self.fake_order_item.product_prices_incl_taxes), numpy.float64
        )

    def test_product_quantity_type(self):
        """
        Test that the product quantity is a int
        """
        self.assertIs(type(self.fake_order_item.product_quantity), int)

    def test_product_variant_type(self):
        """
        Test that the product variant is a FakeProductVariant
        """
        self.assertIs(type(self.fake_order_item.product_variant), FakeProductVariant)

    def test_to_dict_type(self):
        """
        Test that to_dict returns a dict
        """
        self.assertIs(type(self.fake_order_item.to_dict()), dict)

    def test_to_json_type(self):
        """
        Test that to_json returns a valid json
        """
        my_json = self.fake_order_item.to_json()
        self.assertIs(type(my_json), str)
        self.assertIs(is_json(my_json), True)

    def test_configuration_quantity(self):
        """
        test that we can pass quantity kwarg works
        """
        order_item = FakeOrderItem(quantity=4)
        self.assertEqual(order_item.product_quantity, 4)

    def test_composition_variant(self):
        """
        Test that we can composee an order item based on a product variant
        """
        variant = FakeProductVariant()
        order_item = FakeOrderItem(product_variant=variant)
        self.assertEqual(order_item.product_variant, variant)
