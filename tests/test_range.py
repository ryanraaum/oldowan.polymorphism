from oldowan.polymorphism import PolymorphismRange, InfiniteRange
from oldowan.polymorphism import Polymorphism
from nose.tools import raises

def test_polymorphism_range_ints():
    pr = PolymorphismRange((1,10), (20,30))
    assert 1 in pr
    assert 10 in pr
    assert not 15 in pr
    assert 20 in pr
    assert 25 in pr
    assert 30 in pr
    assert not 31 in pr
    assert not -1 in pr
    assert not 0 in pr

def test_polymorphism_range_polys():
    pr = PolymorphismRange((1,10), (20,30))
    # in range
    p0 = Polymorphism(1,0,'A','T')
    p1 = Polymorphism(10,0,'A','T')
    p2 = Polymorphism(20,0,'A','T')
    p3 = Polymorphism(30,0,'A','T')
    p4 = Polymorphism(25,0,'A','T')
    assert p0 in pr
    assert p1 in pr
    assert p2 in pr
    assert p3 in pr
    assert p4 in pr
    # not in range
    p5 = Polymorphism(15,0,'A','T')
    p6 = Polymorphism(0,0,'A','T')
    p7 = Polymorphism(31,0,'A','T')
    p8 = Polymorphism(11,0,'A','T')
    p9 = Polymorphism(1001,0,'A','T')
    assert not p5 in pr
    assert not p6 in pr
    assert not p7 in pr
    assert not p8 in pr
    assert not p9 in pr

def test_infinite_range_ints():
    pr = InfiniteRange()
    assert 1 in pr
    assert 10 in pr
    assert 15 in pr
    assert 20 in pr
    assert 25 in pr
    assert 30 in pr
    assert 31 in pr
    assert -1 in pr
    assert 0 in pr

def test_infinite_range_polys():
    pr = InfiniteRange()
    p0 = Polymorphism(1,0,'A','T')
    p1 = Polymorphism(10,0,'A','T')
    p2 = Polymorphism(20,0,'A','T')
    p3 = Polymorphism(30,0,'A','T')
    p4 = Polymorphism(25,0,'A','T')
    p5 = Polymorphism(15,0,'A','T')
    p6 = Polymorphism(0,0,'A','T')
    p7 = Polymorphism(31,0,'A','T')
    p8 = Polymorphism(11,0,'A','T')
    p9 = Polymorphism(1001,0,'A','T')
    assert p0 in pr
    assert p1 in pr
    assert p2 in pr
    assert p3 in pr
    assert p4 in pr
    assert p5 in pr
    assert p6 in pr
    assert p7 in pr
    assert p8 in pr
    assert p9 in pr

@raises(AttributeError)
def test_polymorphism_range_compare_error():
    p0 = Polymorphism(1,0,'A','T')
    p0=='monkey'


