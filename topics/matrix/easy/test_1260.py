from topics.matrix.easy.problem_1260 import Solution


def test():
    solution = Solution()
    assert solution.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
    assert solution.shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4) == [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
    assert solution.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solution.shiftGrid([[1], [2], [3], [4], [7], [6], [5]], 23) == [[6], [5], [1], [2], [3], [4], [7]]
