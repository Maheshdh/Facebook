class Solution:
    # Time complexity -> O(n)
    # Space complexity -> (2 ^ h)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        if not root:
            return []
        res = []
        queue.append(root)
        while queue:
            cur_nodes_at_level = len(queue)
            for i in range(cur_nodes_at_level):
                front = queue.popleft()
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
                if i == cur_nodes_at_level-1:
                    res.append(front.val)
        return res
