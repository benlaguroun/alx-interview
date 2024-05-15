#!/usr/bin/python3
"""
Solution to the Prime Game problem
"""

def primes(n):
    """
    Return a list of prime numbers between 1 and n (inclusive).
    
    Args:
        n (int): Upper boundary of the range. The lower boundary is always 1.
        
    Returns:
        list: List of prime numbers.
    """
    primes_list = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes_list.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return primes_list

def determine_winner(num_rounds, round_limits):
    """
    Determines the winner of the Prime Game.
    
    Args:
        num_rounds (int): Number of rounds in the game.
        round_limits (list): Upper limits of range for each round.
        
    Returns:
        str: Name of the winner (Maria or Ben), or None if the winner cannot be determined.
    """
    if num_rounds is None or round_limits is None or num_rounds == 0 or not round_limits:
        return None
    
    maria_score = ben_score = 0
    for limit in round_limits:
        prime_numbers = primes(limit)
        if len(prime_numbers) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
            
    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    else:
        return None

