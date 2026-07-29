class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
       rev = "".join(reversed(s[:k]))
       return rev+s[k:]