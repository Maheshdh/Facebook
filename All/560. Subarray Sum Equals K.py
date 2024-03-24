class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        seenPrefix = {0 : 1}
        count = 0
        for i in nums:
            prefix_sum += i
            difference = prefix_sum - k
            if difference in seenPrefix:
                count += seenPrefix[difference]
            seenPrefix[prefix_sum] = seenPrefix.get(prefix_sum,0) + 1
        
        return count
        
        
