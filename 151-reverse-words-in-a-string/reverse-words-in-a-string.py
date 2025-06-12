class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split(" "))
        res = ""
        for i in l:
            if i!="":
                res = i+" "+res
        return res[:-1]