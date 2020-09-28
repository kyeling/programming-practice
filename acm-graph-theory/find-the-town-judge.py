class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        
        count = [0 for _ in range(N+1)]
        
        for p1, p2 in trust:
            count[p1] -= 1
            count[p2] += 1
        
        for i in range(1,N+1):
            if count[i] == N-1:
                return i
            
        return -1
