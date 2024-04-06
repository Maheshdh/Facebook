# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        if not root:
            return []
        queue.append(root)
        result = []
        while queue:
            number_of_nodes = len(queue)
            sum_at_level = 0
            for i in range(number_of_nodes):
                front = queue.popleft()
                sum_at_level += front.val
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            result.append(sum_at_level / number_of_nodes)
        return result


        
