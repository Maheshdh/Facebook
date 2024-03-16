# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,dist_dict,min_dist,max_dist,dist,height):
        if not root:
            return 
        if dist in dist_dict:
            dist_dict[dist].append((root.val,height))
        else:
            dist_dict[dist] = [(root.val,height)]
        min_dist[0] = min(min_dist[0],dist)
        max_dist[0] = max(max_dist[0],dist)
        self.preorder(root.left,dist_dict,min_dist,max_dist,dist-1,height+1)
        self.preorder(root.right,dist_dict,min_dist,max_dist,dist+1,height+1)

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dist = 0
        height = 0
        min_dist, max_dist = [1000],[-1000]
        dist_dict = {}
        self.preorder(root,dist_dict,min_dist,max_dist,dist,height)
        ans = []
        for i in range(min_dist[0],max_dist[0]+1):
            values = dist_dict[i]
            values = sorted(values, key = lambda x: x[1])
            temp = []
            for value in values:
                temp.append(value[0])                     
            ans.append(temp)
        return ans



        
   

        
