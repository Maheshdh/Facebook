# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time complexity -> O(n)
    # space complexity -> O(log(n))
    def height(self,root,diameter):
        if not root:
            return 0
        left_height = self.height(root.left,diameter)
        right_height = self.height(root.right,diameter)
        diameter[0] = max(diameter[0],left_height+right_height)
        return max(left_height,right_height)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = [0]
        self.height(root,diameter)
        return diameter[0]

        
