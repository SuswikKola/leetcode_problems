class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        f = 0
        while c>0 or b>0 or a>0:
            bit= c&1
            c1 = a&1
            c2=b&1
            if (c1|c2)!=bit:
                if bit==1:
                    f+=1
                else:
                    f+=(c1+c2)
            c=c>>1
            a=a>>1
            b=b>>1
        return f
