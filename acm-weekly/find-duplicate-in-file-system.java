class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        HashMap<String, List<String>> map = new HashMap<>();
        for(String path : paths){
            String[] values = path.split(" ");
            for(int i = 1; i < values.length; i++){
                String[] name_cont = values[i].split("\\(");  // split function uses regular expression, same with \\{ and other special characters
                name_cont[1] = name_cont[1].replace(")", "");
                List<String> list = map.getOrDefault(name_cont[1], new ArrayList()); // getOrDefault, if map contains content, returns list, else default triggered (new ArrayList)
                list.add(values[0] + "/" + name_cont[0]);
                map.put(name_cont[1], list); // key: cont, val: list
            }
        }
        List<List<String>> result = new ArrayList<>();
        for(String key : map.keySet()) {
            if(map.get(key).size() > 1){
                result.add(map.get(key));
            }
        }
        return result;
    }
}

/*
map<String, List<String>>
content -> list of files with that content

use Java split function

question asked by Dropbox over phone interview
time O(k * n) where k is max paths and n is max files in path

followups:
what to do if files are really big? hash the files and store the hashcodes instead of the content itself
time it takes to hash the file might take long, what to do next? compare file sizes as a preexisting condition or else can ignore them automatically
*/
