
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])

        output = intervals[0]

        result = []

        for i in range(1,len(intervals)):
            if intervals[i][0] <= output[1]:
                output = [min(output[0],intervals[i][0]),max(intervals[i][1],output[1])]

            else:
                result.append(output)
                output = intervals[i]
            
        result.append(output)

        return result