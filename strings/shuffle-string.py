class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)

# testcase:
# "zerooneoneonetwotwothreethreethreefourfivefivefivefivesixsixsixsixsixseveneighteightnineninenine"
# [73, 55, 78, 63, 17, 54, 23, 67, 11, 52, 46, 62, 12, 9, 42, 31, 61, 71, 81, 68, 72, 15, 91, 90, 39, 24, 36, 18, 79, 93, 37, 77, 0, 95, 92, 27, 7, 34, 28, 75, 47, 64, 65, 25, 51, 57, 6, 30, 32, 13, 38, 1, 21, 40, 26, 45, 8, 20, 89, 59, 86, 49, 4, 84, 2, 35, 69, 50, 58, 3, 10, 80, 53, 94, 76, 19, 70, 74, 82, 87, 88, 14, 48, 85, 22, 5, 44, 66, 33, 41, 43, 16, 60, 83, 29, 56]
    
