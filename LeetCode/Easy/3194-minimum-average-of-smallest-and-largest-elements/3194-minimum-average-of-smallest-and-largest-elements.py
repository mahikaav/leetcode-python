class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        while (len(nums) > 0):
            mini = min(nums)
            maxi = max(nums)
            avg.append((mini+maxi)/2)
            nums.remove(mini)
            nums.remove(maxi)
        return min(avg)
