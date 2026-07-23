class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ctr = 0
        ans = []
        nums.sort()
        for i in range(0,n):
            if (i - ctr - nums[i]) != 0:
                ctr += 1
                ans.append(nums[i])
        
        return ans