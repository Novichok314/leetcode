from topics.trees.easy.problem_100 import Solution, TreeNode


def test():
    solution = Solution()
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))) == True
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(4))) == False
    assert solution.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))) == False