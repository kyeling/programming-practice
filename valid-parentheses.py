class Solution(object):
    def isValid(self, s):
        stack = []
        
        open = ["(", "{", "["]
        close = [")", "}", "]"]
        
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if len(stack) != 0 and open.index(stack[-1]) == close.index(c):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
