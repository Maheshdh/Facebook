class Solution:
    def findrow(self,matrix,target):
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return mid
            elif matrix[mid][0] > target:
                high = mid -1
            else:
                low = mid + 1
        return -1
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowsearch = self.findrow(matrix,target)
        low = 0
        high = len(matrix[0]) - 1
        if rowsearch == -1:
            return False
        while low <= high:
            mid = low + (high - low // 2)
            if matrix[rowsearch][mid] == target:
                return True
            elif matrix[rowsearch][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


        
