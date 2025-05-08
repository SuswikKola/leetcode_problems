class Solution:
    def sortVowels(self, s: str) -> str:
        v = ["a","e","i","o","u"]
        l = list(s)
        res =[]
        for i in range(len(s)):
            if l[i].lower() in v:
                res.append(l[i])
                l[i]=""
        res.sort()
        j=0
        s=""
        for i in range(len(l)):
            if l[i]=="":
                s+=res[j]
                j+=1
            else:
                s+=l[i]
        print(res)
        return s
        