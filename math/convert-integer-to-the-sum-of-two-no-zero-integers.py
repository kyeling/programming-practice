class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n == 2: return [1, 1]
        
        isNoZero = lambda i : "0" not in str(i)

        for i in range(1, n+1):
            if isNoZero(i) and isNoZero(n-i):
                return [i, n-i]


"""
n == 1: not a valid input
n == 2: [1,1] 
n == 3 to 10: [1,n-1]

2-digit numbers containing 0: 10,20,30,...,90
3-digit numbers containing 0: 100,101,102,103,104,105,106,107,108,109,110,120,...,190,
                              200,201,202, etc

if 0 in ones place, add 1
if 0 in tens place, add 10? 11?

brute force:
try [1, n-1] [2, n-2] [3, n-3] ... [9, n-9] [11, n-11] etc and return first one that does not have 0s

max 10,000 (5 digits)
"""
