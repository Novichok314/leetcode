from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        left = 0
        min_len = 1e10
        need = len(freq_t.keys())
        have = 0
        ans = ""
        freq_s = dict()
        for right, sym in enumerate(s):
            freq_s[sym] = freq_s.get(sym, 0) + 1
            if freq_s.get(sym) == freq_t.get(sym, 0):
                have += 1
            while have == need:
                if min_len > right - left + 1:
                    ans = s[left: right + 1]
                    min_len = right - left + 1
                freq_s[s[left]] -= 1
                if freq_s.get(s[left]) < freq_t.get(s[left], -1):
                    have -= 1
                left += 1
        return ans
    
    