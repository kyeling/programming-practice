# Google Foobar Level 3b

import random

# tle probably but can be used to verify solutions
def solution(x, y):
    m, f = int(x), int(y)
    steps = 0
    diff = abs(m-f)
    while diff > 0: 
        print(int(m), int(f), int(diff))
        if m > f: m = diff
        else: f = diff
        steps += 1
        diff = abs(m-f)
    if m == f == 1: return str(steps)
    return 'impossible'

# optimized version of above solution using division to skip repeated increments
def solution_opt(x, y):
    m, f = int(x), int(y)
    diff = abs(m - f)
    tot_steps = 0
    while diff > 0 and m >= 1 and f >= 1: 
        m, f = max(m, f), min(m, f)
        steps =  m // min(f, diff)
        tot_steps += steps
        if diff < f:
            m = diff
            f -= (steps-1) * diff
        else:
            m = m % f
        diff = abs(m-f)
        
    if m == 0 and f == 1: return str(tot_steps-1)
    return 'impossible'

if __name__ == '__main__':
    x = 33
    y = 37
    print(solution(x,y))
    print(solution_opt(x,y))