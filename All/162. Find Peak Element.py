class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        low = 0
        high = N-1
        while low <= high:
            mid = low + (high - low)//2
            if mid == 0:
                return 0 if nums[0] > nums[1] else 1
            if mid == N-1:
                return N-1
            if(nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]):
                return mid
            elif(nums[mid] > nums[mid-1]):
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
