class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i+j].append(nums[i][j])
        result = []
        for key in diagonals.keys():
            result.extend([num for num in diagonals[key][::-1]])
        return result

        
