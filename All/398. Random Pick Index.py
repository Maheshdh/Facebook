class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums        

    def pick(self, target: int) -> int:
        id, count = 0, 0
        for i,num in enumerate(self.nums):
            if num == target:
                count += 1
                probability = random.randint(1,count)
                if probability == count:
                    id = i
        return id
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
