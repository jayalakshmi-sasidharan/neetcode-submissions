class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        for c in s:
            if c in countS:
                countS[c] += 1
            else:
                countS[c] = 1
        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1
            
        return countS == countT
        # return sorted(s) == sorted(t)
        #return Counter(s) == Counter (t)
        # if len(s) != len(t):
        #     return False
        # scount = {}
        # tcount = {}
        # for i in range(len(s)):
        #     scount[s[i]] = 1 + scount.get(s[i],0)
        #     tcount[t[i]] = 1 + tcount.get(t[i],0)
        
        # for c in scount:
        #     if scount[c] != tcount.get(c,0):
        #         return False
        # return True

