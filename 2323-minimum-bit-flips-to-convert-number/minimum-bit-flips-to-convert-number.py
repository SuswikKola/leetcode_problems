class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start^goal
        c=0
        while res:
            c+=res&1
            res>>=1
        return c