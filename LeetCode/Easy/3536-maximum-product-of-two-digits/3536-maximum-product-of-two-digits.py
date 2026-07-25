class Solution:
    def maxProduct(self, n: int) -> int:
        m1, m2 = -1, -1
        while n > 0:
            dig = n%10

            if dig > m1:
                m2 = m1
                m1 = dig

            elif dig > m2:
                m2 = dig

            n = int(n/10)
        
        return m1*m2

