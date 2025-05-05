class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        from queue import PriorityQueue
        q = PriorityQueue()
        for i in nums:
            q.put(i)
        res = []
        while not q.empty():
            t1 = q.get()
            res.append(q.get())
            res.append(t1)
        return res