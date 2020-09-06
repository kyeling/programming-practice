class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> letters = new HashSet<>();
        
        int i = 0; // start ptr
        int j = 0; // end ptr
        int max = 0;
        
        while (j < s.length()) {
            if (!letters.contains(s.charAt(j))) {
                // if unique
                letters.add(s.charAt(j));
                j++;
                max = Math.max(max, letters.size());
            } else {
                // if not unique
                letters.remove(s.charAt(i));
                i++;
            }
        }
        
        /*
        for (int j = 0; j < s.length(); j++) {
            while (letters.contains(s.charAt(j))) {
                letters.remove(s.charAt(j));
                i++;
            }
            letters.add(s.charAt(j));
            max = Math.max(max, letters.size());
        }
        */
        
        return max;
    }
}

/**
Sliding window
i
pwwkew
j
**/
