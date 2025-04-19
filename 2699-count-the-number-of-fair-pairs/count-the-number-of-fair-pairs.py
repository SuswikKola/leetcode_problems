class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        c =0
        while l<r:
            if nums[l]+nums[r]<=upper:
                c+=(r-l)
                l+=1
            else:
                r-=1
        l=0
        r = len(nums)-1
        c_b=0
        while l<r:
            if nums[l]+nums[r]<lower:
                c_b+=(r-l)
                l+=1
            else:
                r-=1
        return c-c_b

