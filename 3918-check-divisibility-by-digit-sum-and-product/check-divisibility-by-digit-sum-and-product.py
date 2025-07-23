class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n1 = n
        s=0
        p=1
        while n1:
            temp = n1%10
            s+=temp
            p*=temp
            n1//=10
        return n%(s+p)==0