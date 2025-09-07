class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        
        result = [neg_num for neg_num in range(-(n-1)//2, 0)] + [pos_num for pos_num in range(1,n//2+1)]
        if n % 2 == 1:
            result += [0]
        return result


"""
if n = 1: [0]
if n is even: return n/2 positive numbers and their corresponding negative numbers
if n is odd: include 0 + n even case

time complexity: O(n) to generate n numbers
space complexity: O(n) to store n numbers in array
"""
