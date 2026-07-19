class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0

        for left in range(len(heights)):
            min_height = heights[left]

            for right in range(left, len(heights)):
                min_height = min(min_height, heights[right])
                width = right - left + 1
                area = min_height * width
                largest = max(largest, area)

        return largest
        