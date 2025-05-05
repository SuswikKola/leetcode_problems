class Solution:
    def frequencySort(self, s: str) -> str:
        dict_a = {}
        for i in s:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        k = dict(sorted(dict_a.items(),key=lambda x:x[1],reverse=True))
        res = ""
        for i in k:
            res+=i*k[i]
        return res