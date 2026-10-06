class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        max_sum = float('-inf')
        start = 0
        counter = {}
        current = 0

        for end in range(len(nums)):
            current += nums[end]
            counter[nums[end]] = counter.get(nums[end],0)+1 

            if end - start + 1 == k:
                if len(counter) == k:
                    max_sum = max(max_sum,current)
                
                current -= nums[start]
                counter[nums[start]] -= 1
                if counter[nums[start]] == 0:
                    del counter[nums[start]]
                
                start += 1
        if max_sum != float('-inf'):
            return max_sum
        return 0        