#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    
    operations = [0] * (n + 1)
    for i in range(2, n + 1):
        if n % i == 0:
            operations[i] = i
            for j in range(i * 2, n + 1, i):
                operations[j] = min(operations[j], operations[i] + j // i)
    
    return operations[n]

if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
