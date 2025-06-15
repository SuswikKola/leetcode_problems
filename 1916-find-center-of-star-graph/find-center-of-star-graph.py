class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dict_a = {}
        for i in edges:
            if i[0] not in dict_a:
                dict_a[i[0]]=1
            else:
                dict_a[i[0]]+=1
            if i[1] not in dict_a:
                dict_a[i[1]]=1
            else:
                dict_a[i[1]]+=1
        for i in dict_a:
            if dict_a[i]==len(dict_a)-1:
                return i