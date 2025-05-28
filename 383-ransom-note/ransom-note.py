class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_a = {}
        dict_b = {}
        for i in ransomNote:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        for i in magazine:
            if i not in dict_b:
                dict_b[i]=1
            else:
                dict_b[i]+=1
        for i in dict_a:
            if i in dict_b and dict_a[i]<=dict_b[i]:
                continue
            else:
                return False
        return True