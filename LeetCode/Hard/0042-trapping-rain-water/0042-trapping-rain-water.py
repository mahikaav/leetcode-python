class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]
        count = 0

        while left < right:
            if right_max < left_max:
                right -= 1
                if right_max > height[right]:
                    count += right_max - height[right]
                else:
                    right_max = height[right]
            else:
                left += 1
                if left_max > height[left]:
                    count += left_max - height[left]
                else:
                    left_max = height[left]
        return count