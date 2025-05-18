class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        dict_a = {}
        for i in range(len(nums)):
            temp = nums[i]
            s = 0
            while temp > 0:
                s += temp % 10
                temp //= 10
            dict_a[nums[i]] = s
        
        sorted_nums = sorted(nums, key=lambda x: (dict_a[x], x))
        index_map = {val: i for i, val in enumerate(sorted_nums)}
        visited = [False] * len(nums)
        swaps = 0
        
        for i in range(len(nums)):
            if visited[i] or index_map[nums[i]] == i:
                continue
            
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = index_map[nums[j]]
                cycle_size += 1
            
            if cycle_size > 1:
                swaps += cycle_size - 1
        
        return swaps
