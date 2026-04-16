from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0: return 0
        
        sCount = Counter(s)
        if (min(sCount.values()) >= k):
            return len(s)
        splitter = next((key for key, val in sCount.items() if val < k))
        return max(self.longestSubstring(_, k) for _ in s.split(splitter))
                    
print(Solution().longestSubstring("ababbc", 2))