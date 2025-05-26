class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = list(sentence.split(" "))
        for i,e in enumerate(l):
            if e.startswith(searchWord):
                return i+1
        return  -1