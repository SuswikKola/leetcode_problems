class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for i in nums:
            res^=i
        k = res^k
        c=0
        while k:
            c+=k&1
            k>>=1
        return c
