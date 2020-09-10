class Solution {
    public int reverse(int x) {
        
        char[] arr = Integer.toString(x).toCharArray();
        int left = 0;
        int right = arr.length - 1;
        
        if (arr[0] == '-') {
            left++;
        }
        
        char temp = ' ';
        while (left < right) {
            temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
        
        long rev = Long.valueOf(String.valueOf(arr));
        if (rev > Integer.MIN_VALUE && rev < Integer.MAX_VALUE) {
            return (int)rev;
        }
        return 0;
        
    }
}


/**
convert int to string
check for neg sign
while left < right
    switch left and right with temp digit
convert to string
**/
