## the next permutation can be found by swapping a pair x,y such that y > x
## this pair should be least significant, so find a pair starting from the end of the array
## once a pair is found, swap the lower value with the first value that is greater than this value from the right
# sort the remaining values to find the lowest permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return []
        pivot = len(nums) - 1
        while pivot > 0:
            if nums[pivot] <= nums[pivot-1]:
                pivot -= 1
            else:
                break
        if pivot != 0:
            a = nums[pivot-1]
            i = len(nums) - 1
            while i > pivot-1:
                if nums[i] <= nums[pivot-1]:
                    i -= 1
                else:
                    break

            nums[pivot-1],nums[i] = nums[i], nums[pivot-1]
            j = len(nums) - 1
            while pivot < j:
                nums[pivot],nums[j] = nums[j],nums[pivot]
                pivot += 1
                j -= 1
        else:
            i = 0
            j = len(nums) - 1
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
        
                    
        
