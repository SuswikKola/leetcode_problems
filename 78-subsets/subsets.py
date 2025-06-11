class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate(i,arr,res,sub):
            if i==len(arr):
                res.append(list(sub))
                return
            sub.append(arr[i])
            generate(i+1,arr,res,sub)
            sub.pop()
            generate(i+1,arr,res,sub)
        res = []
        generate(0,nums,res,[])
        return res
    