"""
Pipelines providing fake orders based on certain conditions

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
import pandas as pd
from consistent_faker.builders import FakeCompanyBuilder
from consistent_faker.builders import FakeCustomerBuilder
from consistent_faker.builders import FakeProductVariantBuilder
from consistent_faker.utils.orders import gen_orders_from_customers_df


def gen_fake_orders(config):
    """
    Pipelines to generate a set of orders based on a pre-defined composition method
    """
    nbr_companies = config.get("number_of_companies")
    nbr_users = config.get("number_of_customers")
    email_deduplication = config.get("email_deduplication")
    nbr_variants = config.get("number_of_variants")

    # Gen Customers
    companies = FakeCompanyBuilder(nbr_companies).build_weights()
    customers = FakeCustomerBuilder(companies, nbr_users, config=config).build_as_dict()
    if email_deduplication:
        customer_df = pd.DataFrame(customers).drop_duplicates(subset="email_address")
    else:
        customer_df = pd.DataFrame(customers)

    # Gen Variants
    variants = FakeProductVariantBuilder(nbr_variants, config=config).build_weights()

    # Gen Orders
    orders = gen_orders_from_customers_df(customer_df, config=config, variants=variants)

    return orders
