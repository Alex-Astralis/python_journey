# Best Time to Buy and Sell Stock (LeetCode #121)

**Pattern:** Sliding Window / One-Pass
**Complexity:** O(n) time, O(1) space

## Problem
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.
You want to maximize your profit by choosing a single day to buy and a different day to sell.

Return the maximum profit. If no profit is possible, return 0.

### Example
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6).

Input: prices = [7,6,4,3,1]
Output: 0
