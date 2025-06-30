class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        k = 0
        maxi = 0
        for i in range(len(nums)):
            while nums[i]-nums[k]>1:
                k+=1
            if nums[i]-nums[k]==1:
                maxi = max(maxi,i-k+1)
        return maxi