class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            ans.append(num)
        i = len(nums)-1
        while i >=0:
            ans.append(nums[i])
            i -= 1
        return ans