#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file
    """
    if not isinstance(n, int) or n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations

if __name__ == "__main__":
    print(minOperations(9))  # Output should be 6

