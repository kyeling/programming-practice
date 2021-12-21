class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to alphanumeric characters only and all lowercase
        alphanumeric = lambda s : ''.join(filter(str.isalnum, s)).lower()
        return alphanumeric(s) == alphanumeric(s[::-1])
