"""
Fake Product Variant builder
-----------------------------
[TODO PLACEHOLDER]
"""
from typing import Optional, List
from consistent_faker.classes import FakeProductVariant
from consistent_faker.builders import FakeBaseBuilderObject


class FakeProductVariantBuilder(FakeBaseBuilderObject):
    """
    TODO
    """

    def __init__(self, n: Optional[int] = None, **kwargs):
        FakeBaseBuilderObject.__init__(self, n=n, **kwargs)
        self._kwargs = kwargs
        self._n = n if n else self.config.get("number_of_variants", 1)

    @property
    def product_variants(self) -> List[FakeProductVariant]:
        """
        Returns:
            List[FakeProductVariant]: list of randomly assigned FakeProductVariant that are built
        """
        return self._build_property

    @product_variants.setter
    def product_variants(self, value: List[FakeProductVariant] = None) -> None:
        """ Setter for product variants"""
        self._build_property = value

    def build(self) -> List[FakeProductVariant]:
        """ build the object """
        self.product_variants = [
            FakeProductVariant(config=self._kwargs.get("config")) for x in range(0, self.n)
        ]
        return self.product_variants
