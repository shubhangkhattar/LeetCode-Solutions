#User function Template for python3

class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        dp_array = [[0]*(W+1) for i in range(n+1)]

        for i in range(1,len(dp_array)):
            for j in range(1,len(dp_array[0])):
                if(wt[i-1] <= j):
                    dp_array[i][j] = max(dp_array[i-1][j],dp_array[i-1][j-wt[i-1]] + val[i-1])
                else:
                    dp_array[i][j] = dp_array[i-1][j]

        return dp_array[-1][-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends