"""
LeetCode 70
Topic: dynamic_programming
Difficulty: easy
"""


class Solution:
    def climbStairs(self, n: int)-> int: 
        if n <= 2: 
            return n 
        curr = 0
        prev1 = 2
        prev2 = 1
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr 

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))
