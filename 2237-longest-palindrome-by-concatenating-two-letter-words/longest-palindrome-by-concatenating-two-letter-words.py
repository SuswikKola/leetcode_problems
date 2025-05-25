class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dict_a = {}
        for i in words:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        l = 0
        dup = []
        for i in dict_a:
            k = i[::-1]
            if k==i:
                dup.append(dict_a[i]) 
            elif (k in dict_a )and (dict_a[i]>0):
                l+=((min(dict_a[i],dict_a[k]))*4)
                dict_a[i]=0
                dict_a[k]=0
        bol = False
        for i in dup:
            temp = i//2
            l+=temp*4
            if i%2==1:
                bol = True
        if bol:
            l+=2
        return l

            
            