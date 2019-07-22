"""
Fake Order builder
-----------------------------
[TODO PLACEHOLDER]
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
