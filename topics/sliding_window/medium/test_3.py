from topics.sliding_window.medium.problem_3 import Solution


def test():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    assert solution.lengthOfLongestSubstring("") == 0
