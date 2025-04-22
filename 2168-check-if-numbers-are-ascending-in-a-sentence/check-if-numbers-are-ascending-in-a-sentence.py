class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = list(s.split(" "))
        res = []
        for i in l:
            if i.isdigit():
                res.append(int(i))
        f = 1
        for i in range(len(res)-1):
            if res[i]<res[i+1]:
                continue
            else:
                f=0
                break
        return True if f==1 else False
        