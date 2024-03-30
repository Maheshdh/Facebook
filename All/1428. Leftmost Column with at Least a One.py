# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        row = 0
        col = cols - 1
        while row < rows and col >=0:
            if binaryMatrix.get(row,col) == 0:
                row += 1
            else:
                print("Row = ",row)
                print("Col = ",col)
                col -= 1
        if col == cols-1:
            return -1 
        else:
            return col + 1
