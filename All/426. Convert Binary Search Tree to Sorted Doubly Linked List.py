"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.first = None
        self.last = None

        self.inorder(root)
        self.first.left = self.last
        self.last.right = self.first
        return self.first
    
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        if not self.last:
            self.first = root
        else:
            root.left = self.last
            self.last.right = root

        self.last = root
        self.inorder(root.right)
        
