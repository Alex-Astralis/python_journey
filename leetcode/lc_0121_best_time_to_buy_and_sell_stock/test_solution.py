import pytest
from leetcode.lc_0121_best_time_to_buy_and_sell_stock.solution import max_profit

def test_example_case():
    assert max_profit([7,1,5,3,6,4]) == 5

def test_descending_prices():
    assert max_profit([7,6,4,3,1]) == 0

def test_constant_prices():
    assert max_profit([3,3,3,3]) == 0

def test_single_day():
    assert max_profit([5]) == 0
