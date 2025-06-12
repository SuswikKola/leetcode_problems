class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        l = 1
        for i in range(1,n):
            l*=nums[i-1]
            res[i]=l
        r = 1
        for i in range(n-2,-1,-1):
            r*=nums[i+1]
            res[i]*=r

        return res
        