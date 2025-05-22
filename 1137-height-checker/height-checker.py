class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        dup = sorted(heights)
        c = 0
        for i in range(len(dup)):
            if heights[i]!=dup[i]:
                c+=1
        return c