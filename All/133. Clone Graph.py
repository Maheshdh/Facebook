"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def clone(self,cur_node,clones):
        if(cur_node in clones):
            return clones[cur_node]
        clones[cur_node] = Node(cur_node.val)
        for neighbor in cur_node.neighbors:
            clones[cur_node].neighbors.append(self.clone(neighbor,clones))
        return clones[cur_node]
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clones = {}
        cloned_origin = self.clone(node,clones)
        return cloned_origin

