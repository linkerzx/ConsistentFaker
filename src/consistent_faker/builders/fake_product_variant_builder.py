"""
Fake Product Variant builder

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
