class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        l , r = 0, len(intervals) - 1
        target = newInterval[0]

        while l <= r:
            mid = (l+r) // 2
            if intervals[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        intervals.insert(l, newInterval)

        res = [intervals[0]]

        for start,end in intervals:
            if res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start,end])
        return res

        