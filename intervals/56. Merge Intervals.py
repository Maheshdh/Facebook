class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting intervals
        intervals = sorted(intervals, key = lambda x : x[0])
        start, end = intervals[0]
        result = []
        for interval in range(1, len(intervals)):
            cur_start, cur_end = intervals[interval]
            if(end >= cur_start):
                end = max(end, cur_end)
            else:
                result.append([start, end])
                start,end = cur_start, cur_end
        result.append([start,end])
        return result

    # [(1,3),(2,6),(8,10),(15,18)]
    # start = 15
    # end = 18
    # cur_start = 15
    # cur_end = 18
    # result = [[1,6],[8,10],[15,18]]

        
