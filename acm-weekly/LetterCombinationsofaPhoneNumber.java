class Solution {
    
    public final String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    
    public List<String> letterCombinations(String digits) {
        List<string> ans = new ArrayList<>();
        if(digits == null || digits.length() == 0) return ans;
        dfs(ans, digits, 0, "");
        return ans;
    }
    
    public void dfs(List<String> ans, String digits, int index, String combination){
        if(index == digits.length()){
            ans.add(combination);
            return;
        }
        // get the letters that the current digit is referring to
        int num = digits.charAt(index) - '0';
        String letters = mapping[num];
        for(char c : letters.toCharArray()){
            dfs(ans, digits, index + 1, combination + c)
        }
    }
}

/*
String[] mappings
mappings[0] = ""
mappings[1] = ""
mappings[2] = "abc"
mappings[3] = "def"

*/
