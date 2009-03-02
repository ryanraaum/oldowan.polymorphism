"""This is the oldowan.polymorphism package."""

import os
version_file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'VERSION'))
version = version_file.read().strip()
version_file.close()

__all__ = ['Polymorphism']

try:
    from oldowan.polymorphism.polymorphism import Polymorphism
except:
    from polymorphism import Polymorphism
