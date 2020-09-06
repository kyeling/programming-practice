class Solution {
    public int search(int[] nums, int target) {
        
        int left = 0;
        int right = nums.length -1;
        int mid;
        
        // find min number
        while (left < right) {
            mid = left + (right - left) / 2;
            // (2 * left + right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        // set bounds 
        if (target > nums[nums.length - 1]) {
            right = left - 1;
            left = 0;
        } else {
            right = nums.length - 1;
        }
        
        // binary search
        while (left <= right) {
            mid = left + (right - left) /2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1;
    }
}

/**
Brainstorming:
- binary search

1. find min number (where sorted part starts)

 0 1 2 3 4 5 6
[4,5,6,7,0,1,2]
        lmr
start = left

2. set bounds for search
check target

3. binary search within bounds

**/
