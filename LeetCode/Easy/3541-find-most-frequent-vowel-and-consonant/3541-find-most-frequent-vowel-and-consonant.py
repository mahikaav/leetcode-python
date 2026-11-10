class Solution:
    def maxFreqSum(self, s: str) -> int:
        hashmap = {}

        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        
        vowels = ['a','e','i','o','u']

        max_cons = 0
        max_vowel = 0

        for x,y in hashmap.items():
            if x in vowels and y > max_vowel:
                max_vowel = y
            elif x not in vowels and y > max_cons:
                max_cons = y
        
        return max_cons + max_vowel