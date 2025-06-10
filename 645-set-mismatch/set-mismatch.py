class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict_a = {}
        ele = 0
        for i in nums:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
                if dict_a[i]==2:
                    ele = i
                    break        
        set_a = set(nums)
        set_b = set(range(1,len(nums)+1))
        inter=  list(set_b-set_a)
        return [ele,inter[0]]