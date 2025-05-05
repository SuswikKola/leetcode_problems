class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        res = [a,b,c]
        res.sort()
        dif1 = (res[1]-res[0])-1
        dif2 = (res[2]-res[1])-1
        m = dif1+dif2
        if (dif1==0 and dif2==0):
            return [0,m]
        elif dif1<=1 or dif2<=1:
            return [1,m]
        return [2,m]
        
