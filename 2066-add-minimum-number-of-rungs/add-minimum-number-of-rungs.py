class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        cur= 0
        if rungs[0]-1>=dist:
            cur+=(rungs[0]-1)//dist
        for i in range(len(rungs)-1):
            if (rungs[i+1]-rungs[i])-1>=dist:
                cur+=(rungs[i+1]-rungs[i]-1)//dist
        return cur
