class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suf = [0]*n
        pref[0]=nums[0]
        suf[-1]=nums[-1]
        for i in range(1,n):
            pref[i]=pref[i-1]*nums[i]
        for i in range(n-2,-1,-1):
            suf[i]=suf[i+1]*nums[i]
        res = []
        for i in range(n):
            if i-1<0:
                res.append(suf[i+1])
            elif i+1==n:
                res.append(pref[i-1])
            else:
                res.append(pref[i-1]*suf[i+1])
        return res
        