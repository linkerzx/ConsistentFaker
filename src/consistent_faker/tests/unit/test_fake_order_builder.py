"""
Unit Test Fake order builder
"""
import unittest
from consistent_faker.builders.fake_order_builder import FakeOrderBuilder
from consistent_faker.classes import FakeOrder


class TestFakeOrderBuilder(unittest.TestCase):
    """
    Unit Test Fake order builder
    """

    def setUp(self):
        self._fake_order_builder_ = FakeOrderBuilder

    @property
    def fake_order_builder_(self):
        """
        Returns Callable FakeOrderBuilder
        """
        return self._fake_order_builder_

    def test_single_generation_types(self):
        """
        Test that the builder is able to generate 1 order type
        """
        test_obj = FakeOrderBuilder(n=1).build()
        self.assertIs(type(test_obj), list)
        self.assertIs(type(test_obj[0]), FakeOrder)

    def test_generation_length(self):
        """
        Test that the builder generates the right amount of FakeOrders
        """
        for i in range(1, 20, 3):
            test_obj = FakeOrderBuilder(n=i).build()
            self.assertIs(len(test_obj), i)

    def test_composition(self):
        """
        TODO test that the order properly imports the customer
        """
