class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict_a = {}
        for i,e in enumerate(s):
            dict_a[e]=i
        res = []
        st = 0
        end = 0
        for i,e in enumerate(s):
            end = max(end,dict_a[e])
            if i==end:
                res.append(end-st+1)
                st=i+1
        return res
        
        