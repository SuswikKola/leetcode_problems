class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n<=k and m<=k:
            return 0
        if n>k and m<=k:
            return (n-k)*(n-(n-k))
        if m>k and n<=k:
            return ((m-k))*(m-(m-k))
        return (n-k)*(n-(n-k))+((m-k)*(m-(m-k)))