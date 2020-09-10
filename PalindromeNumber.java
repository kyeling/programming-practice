class Solution {
    public boolean isPalindrome(int x) {
        
        if (x < 0) {
            return false;
        }
        
        int exp = (int)Math.floor(Math.log10(x));
        int pow = 0;
        int right = 0;
        
        while (exp >= 1) {
            pow = (int)Math.pow(10, exp);
            right = (x - x % pow) / pow;
            if ( right != x % 10 ) {
                return false;
            }
            x -= right * pow;
            x /= 10;
            exp-=2;
        }
        return true;
    }
}

/**
converting int to string:

String str = Integer.toString(x);
        int left = 0;
        int right = str.length() - 1;
        
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
**/
