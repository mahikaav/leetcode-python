class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(0,n,2):
            ans += nums[i]
        for i in range(1,n,2):
            ans -= nums[i]
        return ans            