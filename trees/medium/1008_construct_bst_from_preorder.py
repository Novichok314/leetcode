# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        bst = TreeNode(preorder[0])
        bst.left = self.bstFromPreorder([num for num in preorder if num < preorder[0]])
        bst.right = self.bstFromPreorder([num for num in preorder if num > preorder[0] ])
        return bst
    
Solution().bstFromPreorder([8,5,1,7,10,12])