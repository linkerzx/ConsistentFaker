"""
Fake Sku classs definition
"""
from typing import Dict
from faker import Faker
from consistent_faker.classes import FakeBaseObject

FAKE = Faker()


class FakeSku(FakeBaseObject):
    """
    Generate a random SKU

    Parameters
    -----------
    uid:            Optional[uuid.UUID]
    ean:            Optional[str], product's ean
    title:          Optional[str], product's title
    description:    Optional[str], product's description

    Examples
    -----------
    Generate a random sku
    >>> FakeSku()
    FakeSku(ean=9633372579266, title=capital)

    TODO:
        make a random title more consistent towards products
    """

    def __init__(self, **kwargs):
        """
        initialize FakeSku
        """
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self._ean = kwargs.get("ean", FAKE.format('ean'))
        self._title = kwargs.get("title", FAKE.format('word'))
        self._description = kwargs.get(
            "description", FAKE.format('text')
        )

    def __repr__(self):
        repr_str = f"FakeSku(ean={self.ean}, title={self.title})"
        return repr_str

    @property
    def ean(self) -> str:
        """str: ean"""
        return self._ean

    @property
    def title(self) -> str:
        """str: product title"""
        return self._title

    @property
    def description(self) -> str:
        """str: product description"""
        return self._description

    def to_dict(self) -> Dict:
        """
        Serialize the fake sku object to a dictionary
        """
        sku_dict = {
            "ean": self.ean,
            "title": self.title,
            "description": self.description,
        }
        return sku_dict
