class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # find prefix sum
        # for each index, find the remainder
        # if we already have seen this remainder, that means, the sum between the previous occ and current index is a multiple of k
        remainders = { 0 : -1 }
        running_sum = 0
        for i,value in enumerate(nums):
            running_sum += value
            remainder = running_sum % k
            if remainder in remainders:
                if(i - remainders[remainder] > 1):
                    return True
            else:
                remainders[remainder] = i
        return False
            
        
