from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        uniq = list(set(s))
        maxlen = 0
        
        for letter in uniq:
            q = deque() # queue of indices
            tmplen = 0
            ktmp = k
            for i in range(len(s)):
                if s[i] != letter: # if letter can be flipped, store index, decrement k
                    q.append(i)
                    if ktmp > 0:
                        ktmp -= 1
                    else: # if no operations left, store maxlen, adjust window to after first substring
                        maxlen = max(tmplen, maxlen)
                        tmplen = i - q.popleft() - 1
                tmplen += 1
            maxlen = max(tmplen, maxlen)
        return maxlen
                
            
        
# other cases: ABCDEF, k = 1, 2, ...
# edge case: AAAAA, k = 2 
# AABABBA, k = 2
# edge case: k = 0

# iterate by possible letters in string
# store indices of letters to be switched
# decrement k for each letter switched
# check length of substring when max operations reached
# slide window based on stored indices and take max length

