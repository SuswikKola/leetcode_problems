class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack)==0:
                stack.append(i)
            else:
                if abs(ord(stack[-1])-ord(i))==1:
                    stack.pop()
                elif abs(ord(stack[-1])-ord(i))==25:
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack)==0:
            return ""
        c = ""
        for i in stack:
            c+=i
        return c