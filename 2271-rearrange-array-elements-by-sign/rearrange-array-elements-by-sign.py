class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for i in nums:
            if i>0:
                l1.append(i)
            else:
                l2.append(i)
        res = []
        for i in range(len(l1)):
            res.extend([l1[i],l2[i]])
        return res
