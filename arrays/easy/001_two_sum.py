"""
1. Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Arrays

Approach:
- Проходим по массиву, для каждого элемента проверяем есть ли
  дополнение (target - num) в словаре
- Словарь хранит {значение: индекс}
Time: O(n)
Space: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(s.twoSum([3, 2, 4], 6))         # [1, 2]
    print(s.twoSum([3, 3], 6))            # [0, 1]
