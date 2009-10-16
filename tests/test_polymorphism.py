from oldowan.polymorphism import Polymorphism

def test_polymorphism_compare():
    # equality test should only care about position, insert, and value
    assert(Polymorphism(10,0,'A','T') == Polymorphism(10,0,'A','G'))

    # different insert values are not equal
    assert(Polymorphism(10,0,'A','G') != Polymorphism(10,1,'A','G'))

    # different position values are not equal
    assert(Polymorphism(11,0,'A','G') != Polymorphism(10,0,'A','G'))

def test_polymorphism_to_str():
    assert(str(Polymorphism(10,0,'A')) == '10A')
    assert(str(Polymorphism(10,0,'-')) == '10d')
    assert(str(Polymorphism(10,1,'A')) == '10.1A')

def test_polymorphism_repr():
    assert(repr(Polymorphism(10,0,'A')) == '10A')

def test_polymorphism_is_substitution():
    assert(Polymorphism(10,0,'A').is_substitution())
    assert(not Polymorphism(10,0,'-').is_substitution())

def test_polymorphism_is_transition():
    assert(Polymorphism(10,0,'A','G').is_transition())
    assert(Polymorphism(10,0,'G','A').is_transition())
    assert(Polymorphism(10,0,'C','T').is_transition())
    assert(Polymorphism(10,0,'T','C').is_transition())
    assert(not Polymorphism(10,0,'T','G').is_transition())
    assert(not Polymorphism(10,0,'G','T').is_transition())
    assert(not Polymorphism(10,0,'A','T').is_transition())
    assert(not Polymorphism(10,0,'T','A').is_transition())
    assert(not Polymorphism(10,0,'C','A').is_transition())
    assert(not Polymorphism(10,0,'A','C').is_transition())
    assert(not Polymorphism(10,0,'G','C').is_transition())
    assert(not Polymorphism(10,0,'C','G').is_transition())
    assert(not Polymorphism(10,0,'-','G').is_transition())
    assert(not Polymorphism(10,1,'A','-').is_transition())


def test_polymorphism_is_transversion():
    assert(not Polymorphism(10,0,'A','G').is_transversion())
    assert(not Polymorphism(10,0,'G','A').is_transversion())
    assert(not Polymorphism(10,0,'C','T').is_transversion())
    assert(not Polymorphism(10,0,'T','C').is_transversion())
    assert(Polymorphism(10,0,'T','G').is_transversion())
    assert(Polymorphism(10,0,'G','T').is_transversion())
    assert(Polymorphism(10,0,'A','T').is_transversion())
    assert(Polymorphism(10,0,'T','A').is_transversion())
    assert(Polymorphism(10,0,'C','A').is_transversion())
    assert(Polymorphism(10,0,'A','C').is_transversion())
    assert(Polymorphism(10,0,'G','C').is_transversion())
    assert(Polymorphism(10,0,'C','G').is_transversion())
    assert(not Polymorphism(10,0,'-','G').is_transversion())
    assert(not Polymorphism(10,1,'A','-').is_transversion())

def test_polymorphism_is_insertion():
    assert(not Polymorphism(10,0,'A','G').is_insertion())
    assert(not Polymorphism(10,0,'-','G').is_insertion())
    assert(Polymorphism(10,1,'A','-').is_insertion())

def test_polymorphism_is_deletion():
    assert(not Polymorphism(10,0,'A','G').is_deletion())
    assert(Polymorphism(10,0,'-','G').is_deletion())
    assert(not Polymorphism(10,1,'A','-').is_deletion())

