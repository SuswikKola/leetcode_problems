class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newS = newInterval[0]
        newE = newInterval[1]
        res = []
        f=0
        for si,ei in (intervals):
            if (si<=newS<=ei) or (si<=newE<=ei) or (si>=newS and si<=newE):
                newS = min(newS,si)
                newE = max(newE,ei)
            elif newE<si and f==0:
                res.append([newS,newE])
                f=1
                res.append([si,ei])
            else:
                res.append([si,ei])
        if f==0:
            res.append([newS,newE])
        return res      
