class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0: 
                l = (i==0)or flowerbed[i-1]==0
                r = (i==len(flowerbed)-1) or flowerbed[i+1]==0
                if l and r:
                    flowerbed[i]=1
                    c+=1

        return c>=n
