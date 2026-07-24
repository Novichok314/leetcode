from topics.trees.easy.problem_101 import Solution, TreeNode


def test():
    solution = Solution()
    assert solution.isSymmetric(None) == True
    assert solution.isSymmetric(TreeNode(1)) == True                            
    assert solution.isSymmetric(TreeNode(1, TreeNode(2), TreeNode(2))) == True