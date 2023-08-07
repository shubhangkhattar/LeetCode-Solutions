class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


class Solution:

    # Function to find the maximum number of meetings that can
    # be performed
    # in a meeting room.

    def maximumMeetings(self, n, start, end):

        meetings = [Meeting(start[i],end[i],i) for i in range(n)]

        meetings = sorted(meetings,key=lambda x:(x.end, x.pos))

        count = 1
        end_interval = meetings[0].end
        for meeting in meetings[1:]:
            if meeting.start > end_interval:
                count += 1
                end_interval = meeting.end

        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends