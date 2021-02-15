class Solution {
public:
    void sortColors(vector<int>& nums) {
        
        int tmp = 0;
        int lo = 0;
        int mid = 0;
        int hi = nums.size()-1;
        
        while(mid <= hi){  // <= instead of <
            if(nums[mid] == 0){
                tmp = nums[lo];
                nums[lo] = nums[mid];
                nums[mid] = tmp;
                
                lo++;
                mid++;
            }
            else if(nums[mid] == 1) {
                mid++;
            }
            else if(nums[mid] == 2){
                tmp = nums[hi];
                nums[hi] = nums[mid];
                nums[mid] = tmp;
                
                hi--; // don't decrement mid
            }
        }
        
    }
};
