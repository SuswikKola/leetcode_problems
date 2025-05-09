class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[j].endswith(words[i]) and words[j].startswith(words[i]):
                    c+=1
        return c