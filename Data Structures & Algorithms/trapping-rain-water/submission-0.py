class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)

        for i in range(n):
            maxLeft = 0
            maxRight = 0

            for l in range (i+1):
                maxLeft = max(maxLeft, height[l])
            
            for r in range (i, n):
                maxRight = max(maxRight, height[r])
            
            water = min (maxLeft, maxRight) - height[i]
            total += water
        
        return total