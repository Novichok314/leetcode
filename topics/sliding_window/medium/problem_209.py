"""
LeetCode 209
Topic: arrays
Difficulty: medium
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_len = 1e15
        for right in range(len(nums)):
            window_sum += nums[right] 
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return 0 if min_len == 1e15 else min_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen())
