class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        res = float('inf')
        i=0
        j=i+1
        while j<len(nums):
            if (nums[j]-nums[i])<res:
                res = nums[j]-nums[i]
            i+=1
            j+=1
        return res