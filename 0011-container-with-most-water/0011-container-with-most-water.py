class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0 
        right = len(height) - 1
        max_vol = 0
        while left < right:
            min_height = min(height[left],height[right])
            min_width = right - left
            volume = min_width * min_height
            max_vol = max(volume,max_vol)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_vol