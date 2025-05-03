class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=i+1
        s = nums[j]-nums[i]
        while j<len(nums):
            t = abs(nums[i]-nums[j])
            s = min(t,s)
            i+=1
            j+=1
        return s