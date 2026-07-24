from topics.matrix.medium.problem_200 import Solution


def test():
    solution = Solution()
    assert solution.numIslands(grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]) == 1

    assert solution.numIslands(grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]) == 3
