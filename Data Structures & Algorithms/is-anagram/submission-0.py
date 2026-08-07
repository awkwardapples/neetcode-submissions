class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sHash, tHash = {}, {}

        for i in range(0,len(s)):
            sHash[s[i]] = sHash.get(s[i],0) + 1
            tHash[t[i]] = tHash.get(t[i],0) + 1

        for y in sHash:
            if sHash[y] != tHash.get(y,0):
                return False

        return True




 


        