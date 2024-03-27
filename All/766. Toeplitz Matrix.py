class Solution:
    def validDiagonals(self,row,col,matrix):
        val = matrix[row][col]
        while row < len(matrix) and col < len(matrix[0]):
            if(matrix[row][col] != val):
                return False
            row += 1
            col += 1
        return True

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for col in range(len(matrix[0])):
            if not self.validDiagonals(0,col,matrix):
                return False
        for row in range(1,len(matrix)):
            if not self.validDiagonals(row,0,matrix):
                return False
        return True
        
