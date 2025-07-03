class Solution:
    def kthCharacter(self, k: int) -> str:
        def char_str(s,k):
            if len(s)>=k:
                return s
            dup = ""
            for i in s:
                char = ord(i)+1
                if char>122:
                    dup+="a"
                else:
                    dup+=chr(char)
            s+=dup
            return char_str(s,k)
        c = char_str("a",k)
        return c[k-1]

            