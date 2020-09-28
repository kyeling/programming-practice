class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                if i == n - 1:
                    n -= 1
                    continue
                return count
            else:
                count += 1
        return count
    
# special case: spaces at end of last word
