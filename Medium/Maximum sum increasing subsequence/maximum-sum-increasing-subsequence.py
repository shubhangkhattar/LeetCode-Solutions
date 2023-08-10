#User function Template for python3
class Solution:
    def maxSumIS(self, Arr, n):
        dp_array = Arr[:]
        for i in range(1, n):
            for j in range(i):
                if Arr[i] > Arr[j]:
                    dp_array[i] = max(dp_array[j] + Arr[i], dp_array[i])

        return max(dp_array)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends