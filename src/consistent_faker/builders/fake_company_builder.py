"""
Fake Company builder

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
"""
from typing import List, Optional
from consistent_faker.classes import FakeCompany
from consistent_faker.builders import FakeBaseBuilderObject

class FakeCompanyBuilder(FakeBaseBuilderObject):
    """
    TODO
    """

    def __init__(self, n: Optional[int] = None, **kwargs):
        FakeBaseBuilderObject.__init__(self, n=n, **kwargs)

        if n is None:
            n = self.config.get("number_of_companies", 1)

        self._n = n
        self._build_property = None

    @property
    def companies(self) -> List[FakeCompany]:
        """
        Returns:
            List[FakeOrderItem]: the list of FakeOrderItem that are built
        """
        return self._build_property

    @companies.setter
    def companies(self, value: List[FakeCompany] = None) -> None:
        """ companies setter"""
        self._build_property = value

    def build(self) -> List[FakeCompany]:
        """build """
        self.build_property = [FakeCompany() for x in range(0, self.n)]
        return self.build_property
