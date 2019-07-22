"""
List functions
"""
from typing import List

def flatten(my_list) -> List:
    """list: flatten a list of list"""
    return [item for sublist in my_list for item in sublist]
