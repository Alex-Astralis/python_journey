"""
Great for learning how to use dictionaries (hashes) and clever thinking to make the solution linear time.
"""

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    _dict = {}
    for i, item in enumerate(nums):
        complement = target - item
        if complement in _dict:
            return [i, _dict[complement]]
        _dict[item] = i
    return None

