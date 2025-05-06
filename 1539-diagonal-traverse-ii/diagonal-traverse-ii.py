class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dict_a = {}
        r = len(nums)
        for i in range(r):
            c= len(nums[i])
            for j in range(c):
                k = j+i
                if k not in dict_a:
                    dict_a[k]=[]
                dict_a[k].append(nums[i][j])
        res = []
        for i in dict_a:
            res.extend(dict_a[i][::-1])
        return res