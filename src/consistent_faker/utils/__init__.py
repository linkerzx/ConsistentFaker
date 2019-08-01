"""
Utilility module

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
