from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        left = 0
        anagram_idx = []
        freq_p = Counter(p)
        freq_s = dict()
        need = len(freq_p.keys())
        have = 0
        for right, sym in enumerate(s):
            freq_s[sym] = freq_s.get(sym, 0) + 1
            if freq_s[sym] == freq_p.get(sym, 0):
                have += 1
        
            if right - left + 1 > len(p):
                if freq_s[s[left]] == freq_p.get(s[left], 0):
                    have -=1
                freq_s[s[left]] -=1
                left += 1
        
            if have == need:
                anagram_idx.append(left)
        return anagram_idx
