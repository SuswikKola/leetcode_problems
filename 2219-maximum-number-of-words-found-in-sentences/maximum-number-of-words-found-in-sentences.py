class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for i in sentences:
            l = list(i.split(" "))
            m=max(m,len(l))
        return m