# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        if not root:
            return []
        result = []
        queue.append(root)
        while queue:
            nodes_at_cur_level = len(queue)
            max_val = -float('inf')
            for i in range(nodes_at_cur_level):
                cur_node = queue.popleft()
                if cur_node.val > max_val:
                    max_val = cur_node.val
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            result.append(max_val)
        return result
