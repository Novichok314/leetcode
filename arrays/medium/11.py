class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_cap = 0
        while right >= left:
            if height[left] < height[right]:
                max_cap = max(max_cap, height[left] * (right - left))
                left += 1
            else:
                max_cap = max(max_cap, height[right] * (right - left))
                right -= 1
        return max_cap
