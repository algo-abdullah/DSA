# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.preorder(root,res)
        return res
    def preorder(self,node,res):
        if not node:
            return 
        else:

            res.append(node.val)
            self.preorder(node.left,res)
            self.preorder(node.right,res)
