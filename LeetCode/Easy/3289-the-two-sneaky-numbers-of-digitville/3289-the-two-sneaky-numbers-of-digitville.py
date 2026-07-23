class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n-1):
            if (nums[i+1] - nums[i]) == 0: ans.append(nums[i])
        
        return ans