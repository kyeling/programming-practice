# most common interval problem

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        
        # lambda function = concise way of defining what you want
        intervals = sorted(intervals, key=lambda x: x[0]) # timsort? either way nlogn
        
        res = []
        res.append(intervals[0])
        
        for i in range(1, len(intervals)):
            last = res[-1]
            if last[1] >= intervals[i][0]:
                last[1] = max(last[1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
