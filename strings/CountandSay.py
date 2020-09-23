class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1: return '1'
        prevStr = self.countAndSay(n-1)
        currStr = ''
        streak = 1
        i = 0
        for i in range(len(prevStr)):
            if i+1 < len(prevStr) and prevStr[i] == prevStr[i+1]:
                streak += 1
                continue
            currStr += (str(streak) + prevStr[i])
            streak = 1
        return currStr
