class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict_a = {}
        for i,e in enumerate(groupSizes):
            if e not in dict_a:
                dict_a[e]=[]
            dict_a[e].append(i)
        res = []
        print(dict_a)
        for i in dict_a:
            k = len(dict_a[i])//i
            t =0
            while k:
                temp = dict_a[i][t:t+i]
                res.append(temp)
                t+=i
                k-=1
        return res

                