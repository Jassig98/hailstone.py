# Author: Jasmine Singh
# Github Username: Jassig98
# Date: October 18, 2022
# Description: Hailstone.py

def hailstone (n):
    count=0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count
