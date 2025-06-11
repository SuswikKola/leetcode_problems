class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # res=0
        # for i in nums:
        #     res^=i
        # return res
        set_a = set()
        for i in nums:
            if i not in set_a:
                set_a.add(i)
            else:
                set_a.remove(i)
        l = list(set_a)
        return l[0]