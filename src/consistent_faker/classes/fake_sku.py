"""
Fake Sku classs definition

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
