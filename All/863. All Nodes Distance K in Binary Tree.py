# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        graph = collections.defaultdict(list)
        queue = deque([root])
        while queue:
            front = queue.popleft()
            if front.left:
                graph[front].append(front.left)
                graph[front.left].append(front)
                queue.append(front.left)
            if front.right:
                graph[front].append(front.right)
                graph[front.right].append(front)
                queue.append(front.right)
        
        queue = deque([(target,0)])
        visited = set()
        visited.add((target))
        result = []
        print(queue)
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
            else:
                for neighbor in graph[node]:
                    if not neighbor in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,dist+1))
        return result
            

        
