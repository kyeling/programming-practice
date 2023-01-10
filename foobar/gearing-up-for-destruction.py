# foobar.withgoogle.com Level 2
# kyeling.ong@trulioo.com email

import numpy as np 
from fractions import Fraction 

def solution(pegs): 
    n = len(pegs) 
    A = [[0 for _ in range(n)] for _ in range(n)] 
    b = [0 for _ in range(n)] 
     
    for i, p in enumerate(pegs[:-1]): 
        A[i][i] = 1 
        A[i][i+1] = 1 
        b[i] = pegs[i+1] - pegs[i] 
     
    # requirement that r_initial = 2 * r_final 
    A[n-1][0] = 1 
    A[n-1][n-1] = -2 
     
    A = np.array(A) 
    b = np.array(b) 
    try: 
       res = np.linalg.solve(A,b)
       invalid_res = list(filter(lambda res : res < 1, res))
       if invalid_res: return [-1, -1]
    except: 
        return [-1, -1] 
         
    #convert to simplest form 
    res = Fraction(res[0]).limit_denominator()    
    return [res.numerator, res.denominator]

def main():
    pegs = [1, 999]
    print(pegs)
    print(solution(pegs))

main()