from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        s2Count = dict()
        left = have = 0
        need = len(s1Count)
        for right, sym in enumerate(s2):
            s2Count[sym] = s2Count.get(sym, 0) + 1
            
            if s2Count[sym] == s1Count[sym]:
                have += 1
            
            if right - left + 1 > len(s1):
                if s2Count[s2[left]] == s1Count.get(s2[left], 0):
                    have -= 1
                s2Count[s2[left]] -= 1
                left += 1
    
            if have == need: return True
        return False    