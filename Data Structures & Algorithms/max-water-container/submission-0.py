class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j - i
                h = min (heights[i], heights[j])
                area = width * h
                maxArea = max(maxArea, area)

        return maxArea

        