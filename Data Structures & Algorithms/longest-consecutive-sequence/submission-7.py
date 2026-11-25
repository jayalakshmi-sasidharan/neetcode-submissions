class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = set(nums)
        streak = 0

        for n in nums:
            if n - 1 not in newNums:
                length = 1
                while n + length in newNums:
                    length += 1
                streak = max(streak, length)
        
        return streak
                