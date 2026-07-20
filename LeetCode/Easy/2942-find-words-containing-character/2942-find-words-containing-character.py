class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        i=0
        while i < len(words):
            if x in words[i]:
                ans.append(i)
            i=i+1
        return ans
