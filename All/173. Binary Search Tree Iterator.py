# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left        

    def next(self) -> int:
        next_node = self.stack.pop()
        cur = next_node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return next_node.val        

    def hasNext(self) -> bool:
        return self.stack != []
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
