"""
Unit Tests for Fake Customer Builder

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
