class Solution:
    def numTrees(self, n: int) -> int:
        l = [0]*(n+1)
        l[0]=1
        for i in range(1,n+1):
            for j in range(i):
                l[i]+=l[j]*l[i-1-j]
        return l[n]
        



