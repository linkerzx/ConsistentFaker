"""
Unit Tests for Fake Customer Builder
"""
import unittest
from consistent_faker.builders import FakeCustomerBuilder
from consistent_faker.classes import FakeCustomer


class TestFakeCustomerBuilder(unittest.TestCase):
    """
    Unit Tests for Fake Customer Builder
    """

    def setUp(self):
        self._fake_customer_builder_ = FakeCustomerBuilder

    @property
    def fake_customer_builder_(self):
        """Callable"""
        return self._fake_customer_builder_

    def test_single_generation_type(self):
        """
        Test that the builder is able to generate 1 customer type
        """
        customers = self.fake_customer_builder_(n=1).build()
        self.assertIs(type(customers), list)
        self.assertIs(type(customers[0]), FakeCustomer)

    def test_generation_length(self):
        """
        Test that the builder is able to generate only the right amount of records
        """
        for i in range(1, 30, 3):
            self.assertIs(len(self.fake_customer_builder_(n=i).build()), i)
