class Solution:
    def mirrorDistance(self, n: int) -> int:
        st = str(n)
        rev = int(st[::-1])
        return abs(n-rev) 