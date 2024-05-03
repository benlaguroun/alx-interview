#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    If total is 0 or less, returns 0
    If total cannot be met by any number of coins you have, returns -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    Assumes you have an infinite number of each denomination of coin in the list
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))

