class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        from collections import Counter
        l = list(Counter(nums).values())
        for i in l:
            c=0
            for j in range(2,i+1):
                if i%j==0:
                    c+=1
            if c==1:
                return True
        return False