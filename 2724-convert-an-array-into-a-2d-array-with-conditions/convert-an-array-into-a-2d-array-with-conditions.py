class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dict_a = {}
        for i in nums:
            if i not in dict_a:
                dict_a[i] = 1
            else:
                dict_a[i]+=1
        k =list(sorted(dict_a.items(),key=lambda x:x[1],reverse=True))
        l = []
        for i in range(k[0][1]):
            l.append([])
        for i in k:
            for j in range(i[1]):
                l[j].append(i[0])
        return l