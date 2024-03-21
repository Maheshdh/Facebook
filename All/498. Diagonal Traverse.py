# Approach
# The sum of indices along any diagonal is the same
# for each diagonal represted by it's sum of indices, store each element by traversing the matrix left to right, top to bottom.
# For the zigzag pattern, if the sum of indices is even, we need to reverse the order of elements.
# Time complexity -> O(m*n)
# Space Complexity 0> O(m*n)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        diagonals = {}
        rows, cols = len(mat), len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if((i+j) in diagonals):
                    diagonals[(i+j)].append(mat[i][j])
                else:
                    diagonals[(i+j)] = [mat[i][j]]
        result = []
        for entity in diagonals.items():
            if(entity[0]%2 == 0):
                [result.append(val) for val in entity[1][::-1]]
            else:
                [result.append(val) for val in entity[1]]
        return result
