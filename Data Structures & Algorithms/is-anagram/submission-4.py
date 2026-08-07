class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        shashmap, thashmap = {}, {}

        for char in s:
            shashmap[char] = shashmap.get(char, 0) + 1

        for char in t:
            thashmap[char] = thashmap.get(char, 0) + 1

        return (shashmap == thashmap)