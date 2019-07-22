"""
Unit Tests for Fake order item builder
"""
import unittest
from consistent_faker.builders import FakeOrderItemBuilder
from consistent_faker.classes import FakeOrderItem


class TestFakeOrderItemBuilder(unittest.TestCase):
    """
    Unit tests for Fake order item builder
    """

    def setUp(self):
        self._fake_order_item_builder_ = FakeOrderItemBuilder

    @property
    def fake_order_item_builder_(self):
        """Callable"""
        return self._fake_order_item_builder_

    def test_single_generation_type(self):
        """
        Test that the builder is able to generate 1 order item type
        """
        order_item = self.fake_order_item_builder_(n=1).build()
        self.assertIs(type(order_item), list)
        self.assertIs(type(order_item[0]), FakeOrderItem)

    def test_generation_length(self):
        """
        Test that the builder is able to generate only the right amount of records
        """
        for i in range(1, 30, 3):
            self.assertIs(len(self.fake_order_item_builder_(n=i).build()), i)
