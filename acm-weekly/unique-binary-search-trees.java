class Solution {
    public int numTrees(int n) {
        if(n == 0 || n == 1) return 1; // not necessary here, but good habit to check edge cases
        int[] f = new int[n+1];
        f[0] = 1;
        f[1] = 1;
        for(int i = 2; i <= n; i++){
            // add every possible parent's unique combinations
            for(int j = 0; j < i; j++){
                f[i] += f[j] * f[i-j-1];
            }
        }
        return f[n];
    }
}
