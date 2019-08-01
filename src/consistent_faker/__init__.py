"""
A Library to generate Consistent Fake Data
consistent_faker help you simulate scenarios based on Fake data.

consistent_faker has a couple key features:
- consistency: each object and property is consistent with one another
- configurability: the randomness that is used to generate the fake data
 is configurable using a python dictionary
- composability: objects are composable between each other

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

import os
import json

from consistent_faker.classes import FakeOrder, FakeOrderItem
from consistent_faker.classes import FakePromotion, FakePayment
from consistent_faker.classes import FakeCustomer, FakeBasicCustomer
from consistent_faker.classes import FakeSku, FakeProductVariant
from consistent_faker.classes import FakeCompany
from consistent_faker.classes import FakeEmail
from consistent_faker.classes import FakeAddress

from consistent_faker.builders.fake_company_builder import FakeCompanyBuilder
from consistent_faker.builders.fake_customer_builder import FakeCustomerBuilder
from consistent_faker.builders.fake_order_builder import FakeOrderBuilder
from consistent_faker.builders.fake_order_item_builder import FakeOrderItemBuilder
from consistent_faker.builders.fake_product_variant_builder import FakeProductVariantBuilder

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(FILE_PATH, "configs")


def load_default_config():
    """
    Loads the default configuration dictionary
    """
    default_cfg_path = os.path.join(CONFIG_PATH, "FakeOrdersDefault.json")
    with open(default_cfg_path, "r") as json_file:
        return json.load(json_file)
