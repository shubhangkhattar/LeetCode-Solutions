class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]

        result = []

        for interval in intervals:
            if end >= interval[0]:
                end = max(end,interval[1])
            else:
                result.append([start,end])
                start = interval[0]
                end = interval[1]

        result.append([start,end])
        return result

