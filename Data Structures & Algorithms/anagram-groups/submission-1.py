class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortDict = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)

            if key not in sortDict:
                sortDict[key] = []

            sortDict[key].append(s)

        return list(sortDict.values())
        # sortDict = {}
        
        # for s in strs:
        #     key = "".join(sorted(s))

        #     if key not in sortDict:
        #         sortDict[key] = []

        #     sortDict[key].append(s)
            
        # return list(sortDict.values())
