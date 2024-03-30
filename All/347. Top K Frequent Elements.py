class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        
        for num,count in counts.items():
            freq[count].append(num)
        
        result = []
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                for num in freq[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
        
