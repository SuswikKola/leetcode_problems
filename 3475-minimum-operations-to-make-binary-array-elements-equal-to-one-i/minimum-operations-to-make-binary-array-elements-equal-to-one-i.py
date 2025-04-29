class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)-2):
            if nums[i]==0:
                nums[i]^=1
                nums[i+1]^=1
                nums[i+2]^=1
                c+=1
        return c if nums[len(nums)-1]==1 and nums[len(nums)-2]==1 else -1 