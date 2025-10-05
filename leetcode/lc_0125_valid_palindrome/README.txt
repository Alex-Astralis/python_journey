# Valid Palindrome (LeetCode #125)

**Pattern:** Two Pointers
**Complexity:** O(n) time, O(1) extra space

## Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.

Return `True` if it is a palindrome, or `False` otherwise.

### Example
Input: `s = "A man, a plan, a canal: Panama"`
Output: `True`

Input: `s = "race a car"`
Output: `False`

---

## Approach
1. Use two pointers (start, end).
2. Skip non-alphanumeric characters.
3. Compare lowercase letters/numbers.
4. Stop early if mismatch.

Alternative:
Clean string with regex/filter, then check if `s == s[::-1]`.

---

## Edge Cases
- Empty string → `True`
- Only punctuation → `True`
- Mixed case letters
