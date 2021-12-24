class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    ## OLD solution
        # return sorted(s) == sorted(t)

# sorting: nlogn
# hash map: O(n) space, O(n) time
