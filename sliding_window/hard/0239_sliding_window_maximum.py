from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1: return nums
        
        left = 0
        ans = []
        q = deque()
        for right in range(len(nums)):
            while q and  nums[right] > nums[q[-1]]:
                q.pop()
            
            q.append(right) 
            
            if right - left + 1 == k:
                ans.append(nums[q[0]])
                if left == q[0]:
                    q.popleft()
                left += 1
        return ans

print(Solution().maxSlidingWindow([1,-1], 1))