import heapq
class Solution:
    # Time complexity -> O(nlogk)
    # space complexity -> O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest_el = []
        for i in nums:
            heapq.heappush(k_largest_el,i)
            if len(k_largest_el) > k:
                heapq.heappop(k_largest_el)
        return k_largest_el[0]
