class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        hashset = {}

        while n > 0:
            dig = n%10
            if dig in hashset:
                hashset[dig] += 1
            else:
                hashset[dig] = 1
            
            n = int(n/10)
            
        ans = 0
        for x,y in hashset.items():
            ans += x*y
        
        return ans