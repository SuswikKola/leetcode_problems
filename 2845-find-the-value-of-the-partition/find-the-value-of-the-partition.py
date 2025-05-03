class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        s = nums[1]-nums[0]
        i=1
        j=i+1
        while j<len(nums):
            t = (nums[j]-nums[i])
            s = min(t,s)
            i+=1
            j+=1
        return s