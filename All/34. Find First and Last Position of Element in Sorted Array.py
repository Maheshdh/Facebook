class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1,-1]
        firstIndex = self.findTarget(nums,target,True)
        secondIndex = self.findTarget(nums, target, False)
        return [firstIndex, secondIndex]
    
    def findTarget(self,nums,target,isFirst):
        begin, end = 0, len(nums)-1
        while begin <= end:
            mid = begin + (end-begin)//2
            if(nums[mid] == target):
                if(isFirst):
                    if(begin == 0 and nums[begin] == target):
                        return 0
                    if(nums[mid-1] == target):
                        end = mid -1
                    else:
                        return mid
                else:
                    #print(mid)
                    if(end == len(nums)-1 and nums[end] == target):
                        return end
                    if(nums[mid+1] == target):
                        begin = mid + 1
                    else:
                        print("else = ",mid)
                        return mid
            elif(nums[mid] < target):
                begin = mid +1
            else:
                end = mid -1
        return -1
        
