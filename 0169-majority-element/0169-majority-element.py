class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1

        for key, value in mp.items():
            if value > n: return key
        return 0  
