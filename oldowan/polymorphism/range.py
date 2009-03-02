from types import IntType

class PolymorphismRange(object):
    
    def __init__(self, *range_tuples):
        self.range_tuples = range_tuples

    def __iter__(self):
        yield self

    def __eq__(self, other):
        position = other
        if type(other) != IntType:
            if hasattr(other, "position"):
                position = other.position
            else:
                raise ArgumentError
        for start, end in self.range_tuples:
            if position >= start and position <= end: 
                return True 
        return False


class InfiniteRange(PolymorphismRange):

    def __eq__(self, other):
        if type(other) != IntType and not hasattr(other, "position"):
            raise ArgumentError
        return True
