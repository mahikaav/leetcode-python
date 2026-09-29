class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = len(height)-1
        left = 0
        right = l
        max_water = (right - left)*(min(height[left],height[right]))
        while left < right:
            water = (right - left)*(min(height[left],height[right]))
            max_water = max(water,max_water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water


        