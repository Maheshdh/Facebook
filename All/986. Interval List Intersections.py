class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        s1,s2 = 0 , 0
        mergedList = []
        while s1 < len(firstList) and s2 < len(secondList):
            start1, end1 = firstList[s1]
            start2, end2 = secondList[s2]
            if min(end1,end2) - max(start1,start2) + 1 > 0 :
                mergedList.append([max(start1,start2),min(end1,end2)])
        
            if end1 < start2 or end1 < end2:
                s1 += 1
            else:
                s2 += 1
        return mergedList

        
