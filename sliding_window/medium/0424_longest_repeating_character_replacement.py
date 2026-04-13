class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_freq = 0
        d = dict()
        for right, sym in enumerate(s):
            d[sym] = d.get(sym, 0) + 1
            max_freq = max(max_freq, d[sym])
            while (right - left + 1) - max_freq > k:
                d[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        
        return max_len


Solution().characterReplacement("AABACDDDDDD", 2)