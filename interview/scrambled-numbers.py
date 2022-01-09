import sys
from typing import Counter

scrambled_str = sys.argv[1]

# in order of elimination by unique letters
UNIQ = ['z', 'w', 'u', 'x', 'g', 'o', 't', 'f', 's', 'i'] 
NAME = ['zero', 'two', 'four', 'six', 'eight', 'one', 'three', 'five', 'seven', 'nine'] # English names of numbers
NUMS = ['0', '2', '4', '6', '8', '1', '3', '5', '7', '9'] # Arabic numerals in string form (for multiplication and concatentation)

letters = Counter(scrambled_str)
res = [] # result array to hold numbers, sort at end
occurs = 0  


## replaced with Counter: iterate through input string and fill letters array with frequencies 
# letters = [0] * 26 # array to hold frequencies of letters in input string
# idx = lambda c : ord(c) - ord('a')
# for c in scrambled_str:
#     letters[idx(c)] += 1 


# iterate through UNIQ to check frequencies array for occurrences of unique letters
for i in range(10):
    occurs = letters[UNIQ[i]] # number of occurrences of a unique letter (corresponding to number)
    
    # iterate through string in NAME corresponding to the given number
    # for each character, subtract from its frequency to remove it from input string and count it in result
    for c in NAME[i]: # CONSTANT TIME
        letters[c] -= occurs
    res.append(NUMS[i] * occurs)

print(''.join(sorted(res)))
    
