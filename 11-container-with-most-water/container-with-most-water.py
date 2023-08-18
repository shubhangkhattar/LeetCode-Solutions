class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_volume = 0
        while left < right and left < len(height) and right > 0:
            tank_height = min(height[left],height[right])
            tank_width = right-left
            tank_volume = tank_height * tank_width
            max_volume = max(tank_volume,max_volume)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_volume