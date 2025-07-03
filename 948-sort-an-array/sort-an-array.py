class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeHalves(nums,lo,mid,hi):
            temp = []
            left = lo
            right = mid+1
            while(left<=mid and right<=hi):
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while left<=mid:
                temp.append(nums[left])
                left+=1
            while right<=hi:
                temp.append(nums[right])
                right+=1
            for i in range(lo,hi+1):
                nums[i] = temp[i-lo]
        
        
        def mergeSort(nums,lo,hi):
            if lo==hi:
                return
            mid = (lo+hi)//2
            mergeSort(nums,lo,mid)
            mergeSort(nums,mid+1,hi)
            mergeHalves(nums,lo,mid,hi)
        mergeSort(nums,0,len(nums)-1)
        return nums
        
