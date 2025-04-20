class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        import math
        dict_a = {}
        res = 0
        for i in answers:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        for i in dict_a:
            s = i+1
            groups = math.ceil(dict_a[i]/s)
            res+=groups*s
        return res

