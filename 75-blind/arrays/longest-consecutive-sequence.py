class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        neg_nums = list(filter(lambda x: x < 0, nums))
        pos_nums = list(filter(lambda x: x >= 0, nums))
        
        sorted_nums = []
        if neg_nums:
            abs_value_nums = list(map(lambda x: -1 * x, neg_nums))
            sorted_abs_value_nums = self.radix_sort(abs_value_nums)
            reverse_sorted_neg_nums = list(map(lambda x: -1 * x, sorted_abs_value_nums))
            sorted_nums += reverse_sorted_neg_nums[::-1]
        if pos_nums: 
            sorted_nums += self.radix_sort(pos_nums)
            
        return self.find_longest(sorted_nums)
        
    def radix_sort(self, nums):
        ## RADIX SORT - O(n) time
        if nums == []: return []
        
        digits = int(len(str(max(nums)))) # find largest number and how many digits it has
        sorted_nums = nums
        
        for d in range(digits-1, -1, -1):   # iterate in order of least (rightmost) 
                                            # to most significant digit --> O(digits) time
            hash_table = {i: dict() for i in range(10)}
            for num in sorted_nums: # O(n) time
                                    # make sure to iterate through sorted_nums instead of nums
                bucket_key = int(f"{num:0>{digits}}"[d]) # left-pad with 0s
                hash_table[bucket_key][num] = None       # use dict as an ordered set to deduplicate
            
            sorted_nums = []
            for bucket in hash_table.values(): # O(10) time
                sorted_nums.extend(list(bucket.keys()))
        
        return sorted_nums
    
    def find_longest(self, sorted_nums):
        ## Find longest consecutive sequence from sorted array
        max_streak = 1
        current_streak = 1
        for prev_num, current_num in zip(sorted_nums[:-1], sorted_nums[1:]):
            if prev_num + 1 == current_num:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                print(max_streak, prev_num, current_num)
                current_streak = 1
        max_streak = max(max_streak, current_streak) # update max streak at end of array
        return max_streak
