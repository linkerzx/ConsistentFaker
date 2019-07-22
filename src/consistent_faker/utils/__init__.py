"""
Utilility module
"""

import json
import numpy as np
from faker import Faker
from consistent_faker.weights.domains import TOP_LEVEL_DOMAIN_WEIGHTS
from consistent_faker.utils.random import random_choice_weight_dict
from consistent_faker.utils.random import random_choice_non_normalized_weight_dict
from consistent_faker.utils.lists import flatten
from consistent_faker.utils.orders import gen_orders_from_customers_df

FAKE = Faker()

def get_top_level_domain() -> str:
    """
    Generate a random top level domain
    """
    weights = TOP_LEVEL_DOMAIN_WEIGHTS  # import from default weights
    random_choice = random_choice_weight_dict(weights)
    if random_choice != ".other":
        return random_choice
    tld = "." + FAKE.format('tld')
    while tld in weights.keys():
        tld = "." + FAKE.format('tld')
    return tld


def is_json(myjson):
    """
    Check that myjson is a valid json
    """
    # pylint: disable=unused-variable
    try:
        json_object = json.loads(myjson)
    except ValueError:
        return False
    return True
