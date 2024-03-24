class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        max_ribbon = max(ribbons)
        leftBound = 1
        rightBound = max_ribbon
        result = 0
        while leftBound <= rightBound :
            midVal = leftBound + (rightBound - leftBound)//2
            if(self.canCut(ribbons, midVal, k)):
                result = midVal
                leftBound = midVal + 1
            else:
                rightBound = midVal - 1
        return result
    
    def canCut(self,ribbons,cutLength, k):
        cuts = 0
        for ribbon in ribbons:
            cuts += ribbon // cutLength
        return cuts >= k
        
