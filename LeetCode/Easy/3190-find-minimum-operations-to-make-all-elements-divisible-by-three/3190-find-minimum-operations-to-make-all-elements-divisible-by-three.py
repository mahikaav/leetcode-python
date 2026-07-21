class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i]%3 != 0: ans += 1
        return ans
