class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        cnt = 0
        b = k.bit_length()
        for i,e in enumerate(s[::-1]):
            if e=="1":
                if i<b and res+(1<<i)<=k:
                    res+=1<<i
                    cnt+=1
            else:
                cnt+=1
        return cnt
