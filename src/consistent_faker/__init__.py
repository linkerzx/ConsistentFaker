"""
A Library to generate Consistent Fake Data
consistent_faker help you simulate scenarios based on Fake data.

consistent_faker has a couple key features:
- consistency: each object and property is consistent with one another
- configurability: the randomness that is used to generate the fake data
 is configurable using a python dictionary
- composability: objects are composable between each other
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
