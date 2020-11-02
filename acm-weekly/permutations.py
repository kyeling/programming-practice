# essential problem for backtracking - "all possibilities" means no efficient way around it
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums,[],res)
        return res
    
    def backtrack(self, arr, currPerm, res):
        if not len(arr):
            res.append(currPerm)
        else:
            for i in range(len(arr)):
                newArr = arr[:i] + arr[i+1:] # make new array that excludes curr elem
                newPerm = currPerm + [arr[i]]
                self.backtrack(newArr, newPerm, res)
                
