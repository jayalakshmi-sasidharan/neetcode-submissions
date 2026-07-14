class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0;
        right = len(heights) - 1
        while left < right:

            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            maxArea = max(maxArea, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxArea

        # maxArea = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         width = j - i
        #         h = min (heights[i], heights[j])
        #         area = width * h
        #         maxArea = max(maxArea, area)

        # return maxArea

        