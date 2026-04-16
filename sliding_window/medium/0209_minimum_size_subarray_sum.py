class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        min_len = 1e10
        window_sum = 0
        for right, num in enumerate(nums):
            window_sum += num
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return 0 if min_len == 1e10 else min_len
    

'''
3 — Longest Substring Without Repeating Characters (уже решил)
209 — Minimum Size Subarray Sum
424 — Longest Repeating Character Replacement (уже решил)
438 — Find All Anagrams in a String
567 — Permutation in String
340 — Longest Substring with At Most K Distinct Characters
395 — Longest Substring with At Least K Repeating Characters

Hard (3):

76 — Minimum Window Substring (уже решил)
239 — Sliding Window Maximum
159 — Longest Substring with At Most Two Distinct Characters
'''