from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

# Your data definitions and functions go here.

calpoly_email_addresses = ["mho63@calpoly.edu", "arjohar@calpoly.edu"]

@dataclass(frozen=True)
class GlobeRect:
    lo_lat : float
    hi_lat : float
    west_long : float
    east_long : float

@dataclass(frozen=True)
class Region: 
    rect : GlobeRect
    name : str
    terrain : TypeAlias = Literal['ocean', 'mountain', 'forest', 'other']

@dataclass(frozen=True)
class 


class Tests(unittest.TestCase):
    # Put your test cases in here.
    pass

# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module.
if (__name__ == '__main__'):
    unittest.main()
