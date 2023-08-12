#User function Template for python3

class Solution:

    # Function to return a list containing the DFS traversal of the graph.

    def dfs(self, node, adj, visited, list):
        visited.add(node)
        list.append(node)
        for element in adj[node]:
            if element not in visited:
                self.dfs(element, adj, visited, list)

    def dfsOfGraph(self, V, adj):
        ans = []
        self.dfs(0, adj, set(), ans)
        return ans
        # code here


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends