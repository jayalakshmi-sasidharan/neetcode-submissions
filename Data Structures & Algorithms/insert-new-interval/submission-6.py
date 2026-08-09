class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda pair:pair[0])

        output = [intervals[0]]

        for start, end in intervals:
            if output[-1][1] >= start:
                output[-1] = [min(output[-1][0],start), max( output[-1][1],end)]
            else:
                output.append([start,end])
        
        return output


        