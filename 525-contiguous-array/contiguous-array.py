class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)==2 and sum(nums)==1:
            return 2
        for i,e in enumerate(nums):
            if e==0:
                nums[i]=-1
        for i in range(1,len(nums)):
            nums[i] = nums[i]+nums[i-1]
        h1 = {}
        h2={}
        m = 0
        for i,e in enumerate(nums):
            if e==0:
                m = max(m,i+1)
            if e not in h1:
                h1[e] = i
                h2[e] = i
            else:
                h2[e]=i
        for i in h1:
            m = max(h2[i]-h1[i],m)
        return  m