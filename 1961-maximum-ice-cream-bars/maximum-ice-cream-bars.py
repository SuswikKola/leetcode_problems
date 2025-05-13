class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        count_arr= [0]*(m+1)
        for i in costs:
            count_arr[i]+=1
        res = 0
        for i in range(1,m+1):
            num = min(count_arr[i],coins//i)
            res+=num
            coins-=num*i
            if coins<i:
                break
        return res