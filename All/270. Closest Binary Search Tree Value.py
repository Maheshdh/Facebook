# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = float('inf')
        diff = float('inf')
        cur = root
        while cur:
            cur_diff = abs(cur.val - target)
            if( cur_diff == diff):
                ans = min(ans, cur.val)
            elif(cur_diff < diff):
                ans = cur.val
                diff = cur_diff
            if(cur.val > target):
                cur = cur.left
            else:
                cur = cur.right
        return ans
        
