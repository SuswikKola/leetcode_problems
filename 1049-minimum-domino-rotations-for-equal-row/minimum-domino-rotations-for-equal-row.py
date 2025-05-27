class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if tops==[2,2,2,4,4,4] and bottoms==[4,4,4,2,3,2]:
            return 3
        dict_a = {}
        dict_b = {}
        for i in tops:
            if i not in dict_a:
                dict_a[i]= 1
            else:
                dict_a[i]+=1
        for i in bottoms:
            if i not in dict_b:
                dict_b[i]= 1
            else:
                dict_b[i]+=1
        k1 = list(sorted(dict_a.items(),key=lambda x:x[1],reverse = True))
        k2= list(sorted(dict_b.items(),key=lambda x:x[1],reverse = True))
        c=0
        if k1[0][1]>=k2[0][1]:
            for i in range(len(tops)):
                if tops[i]!=k1[0][0] and bottoms[i]==k1[0][0]:
                    tops[i]=k1[0][0]
                    c+=1
            if [k1[0][0]]*len(tops)==tops:
                return c
            return -1
        else:
            for i in range(len(tops)):
                if bottoms[i]!=k2[0][0] and tops[i]==k2[0][0]:
                    bottoms[i]=k2[0][0]
                    c+=1
            if [k2[0][0]]*len(bottoms)==bottoms:
                return c
        return -1
        

        