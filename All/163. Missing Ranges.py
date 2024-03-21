# traverse through the input array
# check if there is a difference of more than one between consecutive elements
# check boundary cases where lower value or upper value is excluded from the range
# Time complexity -> O(n)
# Space complexity -> O(1)

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[lower,upper]]
        result = []
        if lower < nums[0]:
            result.append([lower,nums[0]-1])
        for i in range(n-1):
            if(nums[i+1]-nums[i]<=1):
                continue
            result.append([nums[i]+1,nums[i+1]-1])
        if upper > nums[-1]:
            result.append([nums[-1]+1,upper])
        
        return result
        
