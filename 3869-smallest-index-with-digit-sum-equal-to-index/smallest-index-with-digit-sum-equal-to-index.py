class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        dict_a = {}
        for i in range(len(nums)):
            temp = nums[i]
            s=0
            while temp>0:
                s+=temp%10
                temp//=10
            if i==s:
                return i
        return -1