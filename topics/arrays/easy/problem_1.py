"""
LeetCode 1
Topic: arrays
Difficulty: easy
"""


class Solution:
    def twoSum(self, nums, target):
        idx_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in idx_map:
                return [idx_map[complement], i]
            idx_map[num] = i


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum())
