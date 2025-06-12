class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict_a = {}
        c=0
        for i in nums:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        for i in nums:
            s = k-i
            if s in dict_a:
                if s!=i:
                    if dict_a[i]>0 and dict_a[s]>0:
                        dict_a[i]-=1
                        dict_a[s]-=1
                        c+=1
                else:
                    if dict_a[s]>1:
                        dict_a[s]-=2
                        c+=1
        return c