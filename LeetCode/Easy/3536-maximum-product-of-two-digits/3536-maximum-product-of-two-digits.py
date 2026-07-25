class Solution:
    def maxProduct(self, n: int) -> int:
        dig = []
        while n != 0:
            dig.append(n%10)
            n = int(n/10)
        
        dig.sort()
        return (dig[-1]*dig[-2])