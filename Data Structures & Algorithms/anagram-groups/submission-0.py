class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortDict = {}
        
        for s in strs:
            key = "".join(sorted(s))

            if key not in sortDict:
                sortDict[key] = []

            sortDict[key].append(s)
            
        return list(sortDict.values())
