class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            value=target - nums[i]
            if value in nums_hash: 
                return [nums_hash[value], i]
            nums_hash[nums[i]] = i
