class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dict_a = {}
        for i in nums:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
                if dict_a[i]>2:
                    return False
        if 2*(len(nums)//2)==len(nums):
            return True
            