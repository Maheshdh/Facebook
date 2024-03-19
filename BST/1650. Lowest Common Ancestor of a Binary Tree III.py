"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_parents = set()
        if not p or not q:
            return None
        p_parents.add(p)
        while p.parent:
            p_parents.add(p.parent)
            p = p.parent
        p_parents.add(p)

        while q:
            if q in p_parents:
                return q
            q = q.parent

        
