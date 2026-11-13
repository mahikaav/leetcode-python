class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        hashmap = {}
        for n in nums:
            if n in hashmap: 
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        add = 0
        for x,y in hashmap.items():
            if y % k == 0: 
                add += x*y
        
        return add