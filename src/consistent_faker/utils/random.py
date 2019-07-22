"""
Random choices functions
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
