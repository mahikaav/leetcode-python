class Solution:
    def maxDistinct(self, s: str) -> int:
        char_set = set(s)
        return len(char_set)
