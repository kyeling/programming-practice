class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
            
        largest_substr = ""
        largest_letter = max(word)
        m = len(word)
            
        for idx, letter in enumerate(word):
            if letter == largest_letter:
                new_substr = word[idx : m-(numFriends-(idx+1))] 
                if new_substr > largest_substr:
                    largest_substr = new_substr  
        
        return largest_substr

"""
gh
numFriends = 1
largest_letter = h
m = 2
special case: if numFriends = 1, return full word instead of starting from highest letter
"""

"""
brute force: find every possible split, and then find largest in lexicographical order
- example word: c1 c2 .... cm
  let m be the length of the word
  let n = numFriends, where n <= m
  word can be split into n susbstrings
- time complexity? exponential? or polynomial?

better solution?
consider the kth split where 1 <= k <= m

workthrough example:
word = "friend", numFriends = "3"
- splits could be f, r, iend
- largest split should start with r
- before r, make as many split as possible
- after r, make the substring as long as possible such that there are still enough letters for the remaining friends

what about double/multiple letters?
another example: "letter", numFriends=3 --> should just return "r"?
"letten" should return "tte"
"tten" should return "tt" (not "te")

what about the letter occurring multiple times but not consecutively?
"tetris", numFriends=3
tetr, i, s
t, e, tris <-- return "tris" as the final answer?

loop through all locations of the letter
worst case: O(n^2) time if word consists of all the same letter
---

what happens if numFriends > len(word)? --> constraint: word.length >= numFriends
what happens if word is empty string? --> constraint: word.length >= 1

how do the rounds work?
start with word --> split --> put splits into box
does the next round start with a new word or does the next word come from the splits?
each friend gets at least one letter in their split

another example: word = "gggg", numFriends = "2"
would the expected result be "ggg"?

clarification on lexicographically largest: "ba" is larger than "aba" even though the first string is shorter? 
"""
