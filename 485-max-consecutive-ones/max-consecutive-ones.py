class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        i=0
        temp = 0
        for i in range(len(nums)):
            if nums[i]==0:
                m=max(temp,m)
                temp=0
            else:
                temp+=1
        m = max(temp,m)
        return m
