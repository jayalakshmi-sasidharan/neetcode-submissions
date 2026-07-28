class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r -l) // 2

            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        return l - 1 if (l and nums[l - 1] == target) else -1

    #     return self.binary_search(0, len(nums) - 1, nums, target)
    
    # def binary_search(self, left: int, right: int, nums: List[int], target):


        # if left > right:
        #     return -1
        
        # mid = (left + right) // 2

        # if nums[mid] == target:
        #     return mid
        
        # if nums[mid] > target:
        #     return self.binary_search(left, mid - 1, nums, target)
        # return self.binary_search(mid+1, right, nums, target)


        
        
        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     mid = (left + right) // 2

        #     if nums[mid] == target:
        #         return mid
            
        #     if nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return -1


        

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        