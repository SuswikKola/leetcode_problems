class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])
        last = intervals[0]
        for i in intervals:
            if i[0]<=last[1]:
                last[1]=max(last[1],i[1])
            else:
                res.append(last)
                last = i
        res.append(last)
        return res