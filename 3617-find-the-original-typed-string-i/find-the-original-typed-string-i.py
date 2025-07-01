class Solution:
    def possibleStringCount(self, word: str) -> int:
        dict_a = {}
        c=1
        for i,e in enumerate(word):
            if e not in dict_a:
                dict_a[e]=1
            elif word[i-1]==e:
                dict_a[e]+=1
                c+=1
        return c