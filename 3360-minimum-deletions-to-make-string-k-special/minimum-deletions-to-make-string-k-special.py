class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        dict_a = {}
        for i in word:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        res= list(sorted(dict_a.values()))
        print(res)
        c = float('inf')
        for i in range(len(res)):
            t = res[i]
            delete = 0
            for j in res:
                if j <t:
                    delete+=j
                elif j>t+k:
                    delete += j-(t+k)
            c = min(c,delete)
        return c