class Solution {
    public int reverse(int x) {
        
        int rev = 0;
        int digit = 0;
        
        while (x != 0) {
            digit = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE && digit > 7) ||
                    rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE && digit < -8 )) {
                return 0;
            }
            rev *= 10;
            rev += digit;
        }
        return rev;
    }
}


/**
get rightmost digit with % 10 then use / 10 to remove it

    before next step, check if greater than MAX / 10
    if equal, check if digit to add is >= 7
multiply digit by power of 10 of right digit

repeat and add new digit * 1 less power of 10 to result

**/


/**
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
**/

/**
convert int to string
check for neg sign
while left < right
    switch left and right with temp digit
convert to string
**/
