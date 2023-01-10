# Google Foobar Level 3c
import sys

import math
def solution(n):
    n = int(n)
    steps = 0
    while n > 3:
        if n % 4 == 0:
            if math.log(n, 2) % 1 == 0: return int(steps + math.log(n, 2))
            steps += 2
            n /= 4
        else:
            steps += 1
            if n % 4 == 1: n -= 1
            elif n % 4 == 2: n /= 2
            else: n += 1
    return int(steps + (n-1))

if __name__ == '__main__':
    n = sys.argv[1]
    print(solution(n))