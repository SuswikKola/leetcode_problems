class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        k = x^y
        c=0
        while k:
            if k&1==1:
                c+=1
            k>>=1
        return c