from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        
        ans = []
        q = deque([root])
        dir_flg = True
        while q:
            lvl = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
                if dir_flg:
                    lvl.append(node.val)
                else:
                    lvl.appendleft(node.val) 
            ans.append(list(lvl))
            dir_flg = not dir_flg 
        return ans