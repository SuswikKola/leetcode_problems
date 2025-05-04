class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = list(s1.split(" "))
        l2 = list(s2.split(" "))
        c = l1+l2
        dict_a = {}
        res = []
        for i in c:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        for i in dict_a:
            if dict_a[i]==1:
                res.append(i)
        return res
