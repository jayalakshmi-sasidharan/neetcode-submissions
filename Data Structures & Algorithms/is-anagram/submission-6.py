class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anaMapS = defaultdict(int)
        anaMapT = defaultdict(int)
        for c in s:
            key = ord(c) - ord('a')
            anaMapS[key] += 1
        for c in t:
            key = ord(c) - ord('a')
            anaMapT[key] += 1
        
        return anaMapS == anaMapT

        