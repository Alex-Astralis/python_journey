from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Return the maximum profit achievable from one buy-sell transaction.

    Args:
        prices (List[int]): Daily stock prices.

    Returns:
        int: Maximum profit; 0 if no profitable trade.
    """

    highest_profit = 0
    min_price = float('inf')

    for price in prices:

        if price < min_price:
            min_price = price
        else:
            highest_profit = max(highest_profit, price - min_price)

    return highest_profit

