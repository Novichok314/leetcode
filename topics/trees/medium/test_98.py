from topics.trees.medium.problem_98 import Solution, TreeNode


def test():
    solution = Solution()
    assert solution.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))) == True
    assert solution.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))) == False
