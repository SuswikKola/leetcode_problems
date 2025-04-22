class Solution:
    def sortSentence(self, s: str) -> str:
        l = list(s.split(" "))
        dup = [""]*len(l)
        for i in l:
            dup[int(i[-1])-1] =i[:-1]
        return " ".join(dup)