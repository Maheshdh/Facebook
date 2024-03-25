class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l , max_ones = 0, 0
        for r, num in enumerate(nums):
            k -= 1 - num

            if( k < 0 ):
                k += 1 - nums[l]
                l += 1
            else:
                max_ones = max(max_ones, r - l + 1)
        return max_ones
        
