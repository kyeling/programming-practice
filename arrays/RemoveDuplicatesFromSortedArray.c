int removeDuplicates(int* nums, int numsSize){    
    if(numsSize == 0) return 0;
    int* start = nums;
    int* replacement = nums + 1;
    int* end = nums + numsSize - 1;
    
    while(replacement <= end){
        if(*replacement == *nums){
            replacement++;
            continue;
        }
        nums++;
        *nums = *replacement;
    }
    return nums - start + 1;
}
