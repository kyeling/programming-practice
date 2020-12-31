class Solution:
    def hammingWeight(self, n: int) -> int:
        wt = 0;
        while n is not 0:
            if n & 1 is 1:
                wt += 1
            n >>= 1
        return wt

# edge cases:
#   0
#   all 1s
#   ood/even numbers and runs of 1s
