# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        if not root:
            return -1
        queue.append(root)
        level = 1
        max_ans = -float('inf')
        max_level = 1
        while queue:
            cur_sum = 0
            nodes_at_cur_level = len(queue)
            for i in range(nodes_at_cur_level):
                cur_node = queue.popleft()
                cur_sum += cur_node.val
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            if cur_sum > max_ans:
                max_ans = cur_sum
                max_level = level
            level+=1
        return max_level
