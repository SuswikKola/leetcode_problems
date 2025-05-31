class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = prev = nums[0]
        for i,e in enumerate(nums[1:]):
            cur = max(0,prev)+e
            ans = max(ans,cur)
            prev = cur
        return ans
