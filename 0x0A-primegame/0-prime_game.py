#!/usr/bin/python3

""" 
Algorithm to determine the winner of the Prime Game in Python
"""

def is_prime(n):
    """ 
    Checks if a given number n is a prime number.
    
    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

def calculate_primes(n, primes):
    """ 
    Calculates all prime numbers up to n and stores them in the given list.

    Args:
        n (int): The upper limit for calculating prime numbers.
        primes (list): A list to store the calculated prime numbers.
    """
    top_prime = primes[-1]
    if n > top_prime:
        for i in range(top_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds in the game.
        nums (list): An array of upper limits for each round.

    Returns:
        str: The name of the player that won the most rounds (Maria or Ben).
        None: If the winner cannot be determined.
    """
    players_wins = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    calculate_primes(max(nums), primes)

    for round_num in range(x):
        sum_options = sum((i != 0 and i <= nums[round_num]) for i in primes[:nums[round_num] + 1])
        if sum_options % 2:
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None

