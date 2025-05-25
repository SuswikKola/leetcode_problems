class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_a = {}
        for i in s:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        bol = False
        l = 0
        for i in dict_a:
            if dict_a[i]%2==0:
                l+=dict_a[i]
            else:
                l+=dict_a[i]-1
                bol=True
        if bol:
            l+=1
        return l
