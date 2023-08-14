#User function Template for python3


from typing import List

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        queue = []
        queue.append(0)
        visited = []
        while queue:
            current_element = queue.pop(0)
            if current_element in visited:
                continue
            visited.append(current_element)
            for element in adj[current_element]:
                if element not in visited:
                    queue.append(element)

        return visited

        # code here
            

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends