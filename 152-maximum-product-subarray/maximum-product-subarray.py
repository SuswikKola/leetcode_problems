
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = [0] * n
        min_prod = [0] * n
        max_prod[0] = min_prod[0] = result = nums[0]

        for i in range(1, n):
            max_prod[i] = max(nums[i], max_prod[i-1] * nums[i], min_prod[i-1] * nums[i])
            min_prod[i] = min(nums[i], max_prod[i-1] * nums[i], min_prod[i-1] * nums[i])
            result = max(result, max_prod[i])

        return result

