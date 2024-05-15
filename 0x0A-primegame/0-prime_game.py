#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win(nums):
        primes = get_primes(max(nums))
        wins = [False] * (max(nums) + 1)
        wins[0] = False
        wins[1] = False
        for i in range(2, len(wins)):
            for p in primes:
                if i % p == 0 and not wins[i - p]:
                    wins[i] = True
                    break
        return wins

    wins = can_win(nums)
    maria_wins = sum(wins[num] for num in nums if wins[num])
    ben_wins = x - maria_wins
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

# Example usage
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))

