from topics.math.easy.problem_2469 import Solution


def test():
    solution = Solution()
    assert solution.convertTemperature(30) == [303.15, 86.0]
    assert solution.convertTemperature(0) == [273.15, 32.0]
    assert solution.convertTemperature(-40) == [233.15, -40.0]