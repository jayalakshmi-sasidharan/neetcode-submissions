class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempMap = {}
        for i in range(len(nums)):
            if target - nums[i] in tempMap:
                return [tempMap[target - nums[i]], i]
            tempMap[nums[i]] = i
        return []
        