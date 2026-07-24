from topics.trees.medium.problem_199 import Solution, TreeNode


def test():
    solution = Solution()
    assert solution.rightSideView(None) == []
    assert solution.rightSideView(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))) == [1, 4, 3]
