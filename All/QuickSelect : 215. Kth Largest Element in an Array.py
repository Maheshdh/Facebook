class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums,k):
            left, mid, right = [],[],[]
            pivot = random.choice(nums)
            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if k <= len(left):
                return quick_select(left,k)
            elif len(left) + len(mid) < k:
                return quick_select(right, k - (len(left) + len(mid)))
            else:
                return pivot
        return quick_select(nums,k)
        
