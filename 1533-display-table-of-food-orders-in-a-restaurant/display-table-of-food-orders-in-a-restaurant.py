class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        index_map = {}
        items = set()
        for i in orders:
            items.add(i[2])
        l = list(items)
        l.sort()
        for i in range(len(l)):
            if l[i] not in index_map:
                index_map[l[i]]=i
        l.insert(0,"Table")
        dict_a = {}
        for i in orders:
            if int(i[1]) not in dict_a:
                dict_a[int(i[1])]=[]
            dict_a[int(i[1])].append(i[2])
        k = dict(sorted(dict_a.items(),key=lambda x:x[0]))
        print(k)
        res = []
        res.append(l)


        for i in k:
            temp = [0]*len(l)
            temp[0]=i
            for j in k[i]:
                temp[index_map[j]+1]+=1
            res1 = map(str,temp)
            res.append(res1)
        return res
