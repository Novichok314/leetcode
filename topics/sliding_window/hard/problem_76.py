from collections import Counter

"""
LeetCode 76
Topic: sliding_window
Difficulty: hard
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        freq_s = {}
        left = 0
        need = len(freq_t.keys())
        have = 0
        ans = ""
        min_len = float("inf")
        for right, sym in enumerate(s): 
            freq_s[sym] = freq_s.get(sym, 0) + 1 
            if sym in freq_t and freq_s[sym] == freq_t[sym]:
                have += 1 

            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1 
                    ans = s[left:right + 1]
                freq_s[s[left]] -= 1
                if s[left] in freq_t and freq_s[s[left]] < freq_t[s[left]]:
                    have -= 1
                left += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
