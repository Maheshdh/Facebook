class Solution:
    def preorder(self,root,ans,low,high):
        if not root:
            return 
        if(root.val < low):
            self.preorder(root.right,ans,low,high)
        if(root.val > high):
            self.preorder(root.left,ans,low,high)
        elif(root.val >= low and root.val <= high):
            ans[0] += root.val
            self.preorder(root.left, ans, low, high)
            self.preorder(root.right,ans,low,high)
        

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        ans = [0]
        self.preorder(root,ans,low, high)
        return ans[0]
