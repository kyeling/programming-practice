class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> seen = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            seen.put(nums[i], i);
        }
        
        for(int i = 0; i < nums.length; i++){
            if(seen.containsKey(target - nums[i]) && seen.get(target - nums[i]) != i){
                return new int[]{i, seen.get(target - nums[i])};
            }
        }
        throw new IllegalArgumentException();
    }
}


//         HashMap<Integer, Integer> seen = new HashMap<Integer, Integer>();
//         int[] soln = new int[2];
        
//         for(int i = 0; i < nums.length; i++) {
//             if(seen.containsKey(target - nums[i])){
//                 soln[0] = i;
//                 soln[1] = seen.get(target - nums[i]);
//             }
//             seen.put(nums[i], i);
//         }
        
//         return soln;


/**
brute force solution:
    for int i in array
        for int j = i+1 to end of array
            check if i + j = target
                if yes, return [i, j]

solution using hashtable:
    for int i in array
        add <index, value> to tbl
        if tbl contains target - value
        return indices of value, target - value
**/
