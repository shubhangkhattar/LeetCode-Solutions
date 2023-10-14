class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        count = 0
        
        end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] < end:
                count += 1
                end = min(interval[1],end)
            else:
                end = interval[1]

        return count