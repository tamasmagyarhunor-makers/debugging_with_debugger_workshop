from lib.bag import *

def test_Bag_instantiates_with_list():
    bag = Bag()
    
    actual = bag.space
    expected = []

    assert actual == expected