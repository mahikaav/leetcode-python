class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        middle_sum = 0
        max_score = float('-inf')
        start = 0
        n = len(cardPoints)
        tot = sum(cardPoints)

        if k == n: 
            return tot

        for end in range(n):
            middle_sum += cardPoints[end]

            if end - start + 1 == n-k:
                max_score = max(max_score, tot-middle_sum)
                middle_sum -= cardPoints[start]
                start += 1
        
        return max_score

