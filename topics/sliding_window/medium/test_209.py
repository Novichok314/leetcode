from topics.sliding_window.medium.problem_209 import Solution


def test():
    solution = Solution()
    assert solution.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]) == 2
    assert solution.minSubArrayLen(target = 4, nums = [1,4,4]) == 1
    assert solution.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]) == 0
