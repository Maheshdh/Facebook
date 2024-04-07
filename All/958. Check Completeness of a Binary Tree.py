# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque()
        queue.append(root)
        null_seen = False
        while queue:
            cur_length = len(queue)
            for i in range(cur_length):
                front = queue.popleft()
                if front.left:
                    if null_seen:
                        return False
                    else:                
                        queue.append(front.left)
                else:
                    null_seen = True
                if front.right:
                    if null_seen:
                        return False
                    else:
                        queue.append(front.right)
                else:
                    null_seen = True
        return len(queue) == 0
        
