class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        s1= ""
        for i in words:
            s1+=i
            if len(s1)==len(s) and s1==s:
                return True

        return False