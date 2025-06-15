class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        intial_node = [0]*(n+1)
        des_node = [0]*(n+1)
        for i in trust:
            des_node[i[1]]+=1
            intial_node[i[0]]+=1
        for i in range(1,n+1):
            if intial_node[i]==0 and des_node[i]==n-1:
                return i
        return -1