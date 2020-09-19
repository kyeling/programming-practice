class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: 
            return ""
        n = len(strs)
    
        # find shortest string
        minLen = len(strs[0])
        for s in strs:
            minLen = min(minLen, len(s))
        
        left = 0
        right = minLen-1
        isCommon = True
        
        while (left <= right):
            mid = left + (right - left) / 2
            for i in range(1, n):
                if strs[0][left:mid+1] != strs[i][left:mid+1]:
                    isCommon = False
            
            if(isCommon):
                left = mid + 1
            else:
                right = mid - 1
            isCommon = True
        
        return strs[0][:right+1]
