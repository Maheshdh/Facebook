class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        result = []
        max_height = heights[-1]
        result.append(len(heights)-1)
        for i in range(len(heights)-1,-1,-1):
            cur_height = heights[i]
            if cur_height > max_height:
                max_height = cur_height
                result.append(i)
        return result[::-1]
