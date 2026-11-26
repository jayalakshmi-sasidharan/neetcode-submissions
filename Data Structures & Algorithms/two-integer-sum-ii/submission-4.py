class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(numbers):
            comp = target - n
            if comp in hashMap:
                return [hashMap[comp], i + 1]
            hashMap[n] = i + 1
        
        return
        