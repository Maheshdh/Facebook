# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = collections.deque()
        if not root:
            return result
        queue.append(root)
        while queue:
            current_level = []
            nodes_at_level = len(queue)
            for i in range(nodes_at_level):
                front = queue.popleft()
                current_level.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            result.append(current_level)
        return result
        
