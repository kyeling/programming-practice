int removeElement(int* nums, int numsSize, int val){
    int* end = nums + numsSize - 1;
    
    while(nums <= end){
        if(*nums == val){
            *nums = *end;
            end--;
            numsSize--;
            continue;
        }
        nums++;
    }
    return numsSize;
}
