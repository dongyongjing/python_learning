# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1 = list()
        def visitroot_middle(root):
            if not root:return
            visitroot_middle(root.left)
            list1.append(root.val)
            visitroot_middle(root.right)
        visitroot_middle(root)
        return list1