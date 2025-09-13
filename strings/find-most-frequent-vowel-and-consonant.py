from collections import Counter

class Solution:
    def maxFreqSum0(self, s: str) -> int:
        letter_freqs = Counter(s)
        max_vowel = max(
            filter(lambda x : x[0] in ['a', 'e', 'i', 'o', 'u'], letter_freqs.items()), 
            key=lambda x: x[1], 
            default=('',0)
        )[1]
        max_consonant = max(
            filter(lambda x : x[0] not in ['a', 'e', 'i', 'o', 'u'], letter_freqs.items()), 
            key=lambda x: x[1],
            default=('',0)
        )[1]
        return max_vowel + max_consonant
        
    def maxFreqSum(self, s: str) -> int:
        """source: nevin-wong"""
        vowels = {}
        consonants = {}
        for char in s:
            if char not in "aeiou":
                if char not in consonants:
                    consonants[char] = 1
                else:
                    consonants[char] += 1
            else:
                if char not in vowels:
                    vowels[char] = 1
                else:
                    vowels[char] += 1
        
        amountVowel = max(vowels.values(), default=0)
        amountConsonants = max(consonants.values(), default=0)
        
        return amountVowel + amountConsonants
