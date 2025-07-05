class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        def min_cost_path(m,n,i,j,waitCost,ans,dp):
            entry = (i+1)*(j+1)
            if i==m-1 and j==n-1:
                return entry
            if i>m-1 or j>n-1:
                return float('inf')
            if dp[i][j]>0:
                return dp[i][j]
            if i==0 and j==0:
                down = min_cost_path(m,n,i+1,j,waitCost,ans,dp)
                right = min_cost_path(m,n,i,j+1,waitCost,ans,dp)
            else:
                down = waitCost[i][j]+min_cost_path(m,n,i+1,j,waitCost,ans,dp)
                right = waitCost[i][j]+min_cost_path(m,n,i,j+1,waitCost,ans,dp)
            dp[i][j] = min(right,down)+entry
            return dp[i][j]
        dp = []
        for i in range(m):
            k = [-1]*n
            dp.append(k)
        return min_cost_path(m,n,0,0,waitCost,0,dp)