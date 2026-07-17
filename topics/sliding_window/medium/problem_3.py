"""
LeetCode 3
Topic: Sliding-window
Difficulty: medium
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str):
        sym = set()
        left = 0
        max_length = 0 

        for right in range(len(s)):
            if s[right] in sym: 
                while s[right] in sym:
                    sym.remove(s[left])
                    left += 1
            sym.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))  # Output: 3
