class Solution:
    # Time Complexity -> O(n)
    # Space Complexity -> O(log(n))
    def preorder(self,root,ans,low,high):
        if not root:
            return 
        # since the node's value is less than the lower range, just traverse the right half of the node, as it could contain values within the range
        if(root.val < low):
            self.preorder(root.right,ans,low,high)
        # similarly traverse only the left half if the node's value is greater than the higher value
        if(root.val > high):
            self.preorder(root.left,ans,low,high)
        # if the node's value is within bounds, we have a valid node. Hence add the value to the result and traverse left and right half.
        elif(root.val >= low and root.val <= high):
            ans[0] += root.val
            self.preorder(root.left, ans, low, high)
            self.preorder(root.right,ans,low,high)
        

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # set intial result as 0 and traverse tree in preorder fashion.
        ans = [0]
        self.preorder(root,ans,low, high)
        return ans[0]
