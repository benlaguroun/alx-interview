#!/usr/bin/python3
"""
Determines the winner of the Prime Game based on given rounds and integer sets
"""

def primes(n):
        """
            Returns a list of prime numbers between 1 and n (inclusive).

                Args:
                        n (int): Upper boundary of the range. The lower boundary is always 1.

                            Returns:
                                    list: List of prime numbers.
                                        """
                                            prime_numbers = []
                                                sieve = [True] * (n + 1)
                                                    for p in range(2, n + 1):
                                                                if sieve[p]:
                                                                                prime_numbers.append(p)
                                                                                            for i in range(p, n + 1, p):
                                                                                                                sieve[i] = False
                                                                                                                    return prime_numbers

                                                                                                                def isWinner(x, nums):
                                                                                                                        """
                                                                                                                            Determines the winner of the Prime Game.

                                                                                                                                Args:
                                                                                                                                        x (int): Number of rounds in the game.
                                                                                                                                                nums (list): List of upper limits of range for each round.

                                                                                                                                                    Returns:
                                                                                                                                                            str: Name of the winner (Maria or Ben), or None if the winner cannot be determined.
                                                                                                                                                                """
                                                                                                                                                                    if x is None or nums is None or x == 0 or not nums:
                                                                                                                                                                                return None
                                                                                                                                                                                
                                                                                                                                                                                maria_wins = ben_wins = 0
                                                                                                                                                                                    for limit in nums:
                                                                                                                                                                                                prime_numbers = primes(limit)
                                                                                                                                                                                                        if len(prime_numbers) % 2 == 0:
                                                                                                                                                                                                                        ben_wins += 1
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                maria_wins += 1
                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                if maria_wins > ben_wins:
                                                                                                                                                                                                                                                                            return 'Maria'
                                                                                                                                                                                                                                                                            elif ben_wins > maria_wins:
                                                                                                                                                                                                                                                                                        return 'Ben'
                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                    return None

                                                                                                                                                                                                                                                                                                # Example usage
                                                                                                                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                        print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
                                                                                                                                                                                                                                                                                                       !/usr/bin/python3
"""
Determines the winner of the Prime Game based on given rounds and integer sets
"""

def primes(n):
    """
    Returns a list of prime numbers between 1 and n (inclusive).

    Args:
        n (int): Upper boundary of the range. The lower boundary is always 1.

    Returns:
        list: List of prime numbers.
    """
    prime_numbers = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime_numbers.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime_numbers

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): Number of rounds in the game.
        nums (list): List of upper limits of range for each round.

    Returns:
        str: Name of the winner (Maria or Ben), or None if the winner cannot be determined.
    """
    if x is None or nums is None or x == 0 or not nums:
        return None
    
    maria_wins = ben_wins = 0
    for limit in nums:
        prime_numbers = primes(limit)
        if len(prime_numbers) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
            
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))

