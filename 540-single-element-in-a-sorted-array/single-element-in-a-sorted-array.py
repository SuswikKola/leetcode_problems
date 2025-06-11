class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h=len(nums)-1
        while l<h:
            mid = (l+h)//2
            if mid%2==1:
                mid-=1
            if nums[mid]!=nums[mid+1]:
                h = mid
            else:
                l = mid+2
        return nums[l]
            
       