"""
Util to generate orders for some customers

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
import numpy as np
from consistent_faker.utils.lists import flatten


def gen_orders_from_customers_df(customer_df, config=None, variants=None):
    """
    Util to generate orders for some customers given a given product catalogue
    and configuration dictionary
    """
    output = []

    from consistent_faker.classes import FakeCustomer
    from consistent_faker.builders.fake_order_builder import FakeOrderBuilder

    max_orders_per_cust = config.get("max_orders_per_cust", 15)
    min_orders_per_cust = config.get("min_orders_per_cust", 0)

    for row in customer_df.iterrows():
        fake_customer = FakeCustomer(**row[1])
        number_of_orders = np.random.randint(
            low=min_orders_per_cust, high=max_orders_per_cust
        )
        fake_order = FakeOrderBuilder(
            fake_customer, number_of_orders, config=config, variants=variants
        ).build()
        output.append(fake_order)
    return [x for x in flatten(output)]
