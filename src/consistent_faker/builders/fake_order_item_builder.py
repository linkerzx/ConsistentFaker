"""
Fake Order Item builder
-----------------------------
[TODO PLACEHOLDER]
"""
from typing import List, Dict
from consistent_faker.classes import FakeOrderItem, FakeProductVariant
from consistent_faker.builders import FakeBaseBuilderObject


class FakeOrderItemBuilder(FakeBaseBuilderObject):
    """
    Generates a list of order items based on the provided parameters

    Parameters
    -----------
    n:          Optional[int], the number of order items that are set to be built
    config:     Optional[Dict]
    variants:   Optional[Dict[FakeProductVariant, np.float64]]
    """

    def __init__(self, n: int = 1, **kwargs) -> None:
        FakeBaseBuilderObject.__init__(self, n=n, **kwargs)
        self._variants = kwargs.get("variants")
        self._n = n

    @property
    def variants(self) -> Dict[FakeProductVariant, float]:
        """
        Returns:
            Dict[FakeProductVariant, float]: variant dict
            that were are used to generate the order items
        """
        return self._variants

    @property
    def order_items(self) -> List[FakeOrderItem]:
        """
        Returns:
            List[FakeOrderItem]: the list of FakeOrderItem that are built
        """
        return self._build_property

    @order_items.setter
    def order_items(self, value: List[FakeOrderItem] = None) -> None:
        """ order item setter """
        self._build_property = value

    def build(self) -> List[FakeOrderItem]:
        """ build """
        self.order_items = [
            FakeOrderItem(config=self.config, variants=self.variants)
            for x in range(0, self.n)
        ]
        return self.order_items
