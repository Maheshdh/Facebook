class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = []
        for i,num in enumerate(nums):
            if num != 0:
                self.array.append((i,num))
                    
        
# ob1 = SparseVector(None)
# ob1.dotProduct(None)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if(len(self.array) == 0 or vec is None or vec.array == 0):
            return 0
        result = 0
        p_org, p_obj = 0 ,0 
        while p_org < len(self.array) and p_obj < len(vec.array):
            if self.array[p_org][0] == vec.array[p_obj][0]:
                result += self.array[p_org][1] * vec.array[p_obj][1]
                p_org += 1
                p_obj += 1
            elif self.array[p_org][0] < vec.array[p_obj][0]:
                p_org += 1
            else:
                p_obj += 1
        return result 


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
