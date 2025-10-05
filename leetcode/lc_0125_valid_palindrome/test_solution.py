import pytest
from leetcode.lc_0125_valid_palindrome.solution import is_palindrome

def test_valid_palindrome_basic():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_valid_palindrome_false():
    assert is_palindrome("race a car") is False

def test_valid_palindrome_empty():
    assert is_palindrome("") is True

def test_valid_palindrome_punctuation_only():
    assert is_palindrome(".,;!!") is True