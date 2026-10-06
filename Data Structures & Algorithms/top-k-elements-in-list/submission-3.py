class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for c in nums:
            freqMap[c] = freqMap.get(c, 0) + 1
        
        freqMap = sorted(freqMap, key = freqMap.get, reverse = True)
        return freqMap[:k]

        