# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1 = list()
        def vistroot_behind(root):
            if not root:return
            vistroot_behind(root.left)
            vistroot_behind(root.right)
            list1.append(root.val)
        vistroot_behind(root)
        return list1