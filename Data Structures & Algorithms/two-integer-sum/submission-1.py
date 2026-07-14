class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newset = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in newset:
                return [newset[complement], i]
            newset[num] = i
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]
        
        # return null
        