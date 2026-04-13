class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pair = dict()
        for idx, num in enumerate(nums):
            diff = target - num 
            if diff in pair:
                return [pair[diff], idx]
            pair[num] = idx
