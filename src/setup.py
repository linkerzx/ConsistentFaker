#!/usr/bin/env python
"""
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
from setuptools import setup, find_namespace_packages


setup(
    name="consistent_faker",
    version="0.1",
    description="consistent_faker, Fake your data consistantly",
    author="Julien Kervizic",
    author_email="julien.kervizic@gmail.com",
    url="placeholder.com",
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=0.24.1",
        "numpy>=1.15.4",
        "Faker>=1.0.5",
        "pycountry>=18.12.8",
        "tld>=0.9.3",
        "email-validator>=1.0.4",
    ],
)
