class Solution:
    def maxProduct(self, n: int) -> int:
        l = []
        for i in str(n):
            l.append(int(i))
        l.sort(reverse=True)
        if n<10:
            return n
        else:
            return l[0]*l[1]