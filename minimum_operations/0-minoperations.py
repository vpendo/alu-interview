#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the number of operations needed to result n H character
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations


if __name__ == "__main__":
    n = 4
    message = "Min # of operations to reach {} char: {}"
    print(message.format(n, minOperations(n)))

    n = 12
    print(message.format(n, minOperations(n)))
