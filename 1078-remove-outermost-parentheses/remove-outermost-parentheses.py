class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        outer = 0
        res=""
        for i in s:
            if i=="(":
                if outer>0:
                    res+=i
                outer+=1
            else:
                outer-=1
                if outer>0:
                    res+=i
        return res
