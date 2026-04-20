from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        numOfIslands = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    q.append((i, j))
                    while q:
                        x, y = q.pop()
                        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            nx, ny = x + dx, y + dy 
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                                q.append((nx, ny))
                                grid[nx][ny] = '0'
                    numOfIslands += 1
        return numOfIslands

        