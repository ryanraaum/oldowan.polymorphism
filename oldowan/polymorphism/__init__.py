"""This is the oldowan.polymorphism package."""

import os

VERSION = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'VERSION')).read().strip()

__all__ = ['Polymorphism',
           'PolymorphismRange',
           'InfiniteRange']

try:
    from oldowan.polymorphism.polymorphism import Polymorphism
    from oldowan.polymorphism.range import PolymorphismRange
    from oldowan.polymorphism.range import InfiniteRange
except:
    from polymorphism import Polymorphism
    from range import PolymorphismRange
    from range import InfiniteRange
