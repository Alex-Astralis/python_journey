import pytest
from two_sum_solution import two_sum

def test_two_sum_example():
    assert two_sum([2,7,11,15], 9) in ([0,1],[1,0])

def test_two_sum_negatives():
    assert two_sum([-3,4,3,90], 0) in ([0,2],[2,0])

def test_two_sum_duplicates():
    assert two_sum([3,3], 6) == [1,0] or [0,1]

def test_two_sum_no_solution():
    assert two_sum([1,2,3], 7) == []