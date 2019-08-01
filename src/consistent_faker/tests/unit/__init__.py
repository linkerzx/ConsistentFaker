"""
Consistent Faker Unit tests

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
from consistent_faker.tests.unit.test_fake_payment import TestFakePayment
from consistent_faker.tests.unit.test_fake_company import TestFakeCompany
from consistent_faker.tests.unit.test_fake_address import TestFakeAddress
from consistent_faker.tests.unit.test_fake_sku import TestFakeSku
from consistent_faker.tests.unit.test_fake_promotion import TestFakePromotion
from consistent_faker.tests.unit.test_fake_product_variant import TestFakeProductVariant
from consistent_faker.tests.unit.test_fake_email import TestFakeEmail
from consistent_faker.tests.unit.test_fake_customer import TestFakeCustomerBasicTypes
from consistent_faker.tests.unit.test_fake_customer import TestFakeCustomerComposition
from consistent_faker.tests.unit.test_fake_order_item import TestFakeOrderItem
from consistent_faker.tests.unit.test_fake_order import TestFakeOrderBasicTypes
from consistent_faker.tests.unit.test_fake_order import TestFakeOrderMath
from consistent_faker.tests.unit.test_fake_order import TestFakeOrderComposition
from consistent_faker.tests.unit.test_fake_company_builder import TestFakeCompanyBuilder
from consistent_faker.tests.unit.test_fake_order_builder import TestFakeOrderBuilder
from consistent_faker.tests.unit.test_fake_customer_builder import (
    TestFakeCustomerBuilder,
)
from consistent_faker.tests.unit.test_fake_order_item_builder import (
    TestFakeOrderItemBuilder,
)
