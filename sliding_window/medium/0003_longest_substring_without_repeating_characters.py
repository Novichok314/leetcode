class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] in s[left:right]:
                while s[left] != s[right]:
                    left += 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len
