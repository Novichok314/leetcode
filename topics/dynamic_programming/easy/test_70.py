from topics.dynamic_programming.easy.problem_70 import Solution


def test():
    solution = Solution()
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
    assert solution.climbStairs(4) == 5
    assert solution.climbStairs(5) == 8
    assert solution.climbStairs(6) == 13
    assert solution.climbStairs(7) == 21