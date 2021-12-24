class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs] # if strs only has one string, it's its own anagram

        sorted_strs = {} # approach: dictionary with sorted strs as key and groups of anagrams as values
        for s in strs:
            key = ''.join(sorted(s)) # need to join because sorted returns a list of chars, which is not hashable!!
            # if key in sorted_strs:
            #     sorted_strs[key].append(s) # if existing anagram, append to existing list
            # else:
            #     sorted_strs[key] = [s] # if new anagram, create new list
            sorted_strs[key] = sorted_strs.get(key, []) + [s] # faster way to achieve the commented out section
        return sorted_strs.values()
        
        
        
## OLD approach        
#         counters = [] # array to hold Counter objects for each string
#         groups = [] # result array to hold groups of anagrams
#         for s in strs:
#             key = Counter(s)
#             if key in counters: # if Counter already in list, group with existing anagram
#                 groups[counters.index(key)].append(s)
#             else: # otherwise, add Counter to list and create a new group
#                 counters.append(key)
#                 groups.append([s])
        
#         return groups
        
# brute force:
# for each string, check all other strings to see if they are anagrams
