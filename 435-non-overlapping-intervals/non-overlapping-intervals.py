class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        end = intervals[0][1]
        
        del_count = 0

        for interval in intervals[1:]:
            if interval[0] < end:
                del_count += 1
                end = min(end,interval[1])
            else:
                end = interval[1]

        return del_count