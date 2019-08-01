"""
Fake Order builder

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
from typing import List
from consistent_faker.classes import FakeOrder
from consistent_faker.classes import FakeCustomer, FakeProductVariant
from consistent_faker.builders import FakeBaseBuilderObject


class FakeOrderBuilder(FakeBaseBuilderObject):
    """
    Generates a list of orders based on the provided parameters

    Parameters
    -----------
    n:          Optional[int], the number of order that are set to be built
    customer:   Optional[FakeCustomer]
    config:     Optional[Dict]
    variants:   Optional[Dict[FakeProductVariant, float]]
    """

    def __init__(self, customer: FakeCustomer = None, n: int = 1, **kwargs) -> None:
        FakeBaseBuilderObject.__init__(self, n=n, **kwargs)
        self._customer = customer if customer else None
        self._n = n
        self._variants = kwargs.get("variants")

    @property
    def orders(self) -> FakeOrder:
        """
        Returns:
            List[FakeOrder]: the list of FakeOrder that are built
        """
        return self._build_property

    @orders.setter
    def orders(self, value: List[FakeOrder] = None):
        """settter for orders"""
        self._build_property = value

    @property
    def customer(self) -> FakeCustomer:
        """
        Returns:
            FakeCustomer: that is associated with the orders
        """
        return self._customer

    @property
    def variants(self) -> FakeProductVariant:
        """
        Returns:
            FakeProductVariant: that were are used to generate the order
        """
        return self._variants

    def build(self) -> List[FakeOrder]:
        """ build """
        self.orders = [
            FakeOrder(self.customer, config=self.config, variants=self.variants)
            for x in range(0, self.n)
        ]

        return self.orders
