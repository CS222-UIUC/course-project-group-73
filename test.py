import calc
from genre_classifier import *


def test_load_data() :
    inputs, targets = load_data("data.json")
    assert(len(inputs) == 2000)
    for i in targets:
        assert (0 <= i <= 9)
    

test_load_data()

print("all test cases passed")
