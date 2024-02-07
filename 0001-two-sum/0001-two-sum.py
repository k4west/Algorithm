class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_nums = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in d_nums:
                return [d_nums[comp], i]
            d_nums[num] = i