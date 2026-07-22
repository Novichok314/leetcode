from topics.math.easy.problem_2235 import Solution


def test():
    solution = Solution()
    assert solution.sum(2, 3) == 5
    assert solution.sum(-1, 1) == 0
    assert solution.sum(0, 0) == 0
    