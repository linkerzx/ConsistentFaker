"""
Unit Test Fake order builder

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
