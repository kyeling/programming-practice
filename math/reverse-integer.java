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
