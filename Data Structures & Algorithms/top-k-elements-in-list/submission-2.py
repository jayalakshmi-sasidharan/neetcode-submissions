class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)

        result = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        # countingDict = {}
        # for n in nums:
        #     countingDict[n] = 1 + countingDict.get(n, 0)

        # arr = sorted(
        #     countingDict.items(),
        #     key = lambda x:x[1],
        #     reverse = True
        # )
        
        # result = []

        # for num, freq in arr[:k]:
        #     result.append(num)

        # return result
