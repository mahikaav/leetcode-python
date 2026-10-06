class Solution:
    def minRotations(self, s: str) -> int:
        count = 0
        prev = 0

        for i in s:
            int_i = int(i)
            diff = abs(prev-int_i)
            count += min(diff, 10-diff)
            prev = int_i
        return count