class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if (i%2==0):
                ans = ans + nums[i]
            else: 
                ans = ans - nums[i]
        return ans            