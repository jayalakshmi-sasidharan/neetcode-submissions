class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n == 0:
            return 0
        
        maxLeft = [0] * n
        maxRight = [0] * n

        maxLeft[0] = height[0]
        maxRight[n-1] = height[n-1]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])

        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i]) 
        
        total = 0

        for i in range(n):
            total += min(maxLeft[i], maxRight[i]) - height[i]
        
        return total


        # total = 0
        # n = len(height)

        # for i in range(n):
        #     maxLeft = 0
        #     maxRight = 0

        #     for l in range (i+1):
        #         maxLeft = max(maxLeft, height[l])
            
        #     for r in range (i, n):
        #         maxRight = max(maxRight, height[r])
            
        #     water = min (maxLeft, maxRight) - height[i]
        #     total += water
        
        # return total