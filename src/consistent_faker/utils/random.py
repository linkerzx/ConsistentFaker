"""
Random choices functions

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


def random_choice_weight_dict(weight_dict: dict) -> str:
    """
    Randomly selected a key based on the weighted dict
    It requires the weights to be normalized (ie: summing to 1)
    Returns:
        str: key selected at random
    """
    weights = weight_dict
    choices = list(weights.keys())
    return np.random.choice(choices, p=list(weights.values()))


def random_choice_non_normalized_weight_dict(weight_dict: dict) -> str:
    """
    Randomly selected a key based on a non-weighted dict
    It does not requires the weights to be normalized (ie: summing to 1)
    Returns:
        str: key selected at random
    """
    weights = weight_dict
    choices = list(weights.keys())
    proba = [x / sum(weights.values()) for x in list(weights.values())]
    return np.random.choice(choices, p=proba)
