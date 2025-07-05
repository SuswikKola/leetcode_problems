class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict_a = {}
        for i in arr:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        m = -1
        for i in dict_a:
            if i==dict_a[i]:
                m = max(m,i)
        return m
