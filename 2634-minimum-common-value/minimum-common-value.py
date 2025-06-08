class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        dict_a = {}
        for i in nums1:
            if i not in dict_a:
                dict_a[i]=1
        for i in nums2:
            if i in dict_a:
                return i
        return -1