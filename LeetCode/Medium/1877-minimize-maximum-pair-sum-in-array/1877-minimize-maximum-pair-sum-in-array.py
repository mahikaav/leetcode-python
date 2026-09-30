class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        left = 0
        right = len(nums)-1
        while left < right:
            ans.append(nums[left] + nums[right])
            left += 1
            right -= 1

        return max(ans)
        