class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i - 1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result

        # result = []
        # product = 1
        # for i in nums:
        #     product *= i
        
        # for i in range(len(nums)):
        #     result.append(int(product/nums[i]))

        # return result

        # result = []
        # for i in range(len(nums)):
        #     product = 1

        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]

        #     result.append(product)
        # return result