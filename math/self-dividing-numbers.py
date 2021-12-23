class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            isSelfDiv = True
            for dig in set(str(num)):
                if int(dig) == 0 or (int(dig) != 1 and num % int(dig) != 0):
                    isSelfDiv = False
                    continue
            if isSelfDiv:
                res.append(num)
        return res
        
# brute force approach:
# for each number in range:
#   for each digit in number:
#       check if number mod digit = 0

# optimizations?
# skip repeated digits
# skip single digit numbers
# skip digit 1

# edge case: divide by zero
