from topics.sliding_window.hard.problem_76 import Solution


def test():
    solution = Solution()
    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert solution.minWindow("a", "a") == "a"
    assert solution.minWindow("a", "aa") == ""
    assert solution.minWindow("ab", "b") == "b"
