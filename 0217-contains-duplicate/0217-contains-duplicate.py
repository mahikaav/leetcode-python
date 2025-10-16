class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        
        for key, value in mp.items():
            if value > 1: return True
        return False 