class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        l = []
        l.append(s[0])
        c=0
        for i in range(1,len(s)):
            l.append(l[-1]+s[i])
        for i in words:
            if i in l:
                c+=1
        return c