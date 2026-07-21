"""
LeetCode 1260
Topic: matrix
Difficulty: easy
"""


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        size = m * n
        ans = [[0 for _ in range(n)] for _ in range(m)] 
        for i in range(size): 
            row = i // n 
            col = i % n
            new_row = ((i + k) // n) % m
            new_col = (i + k) % n
            ans[new_row][new_col] = grid[row][col]
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9))
