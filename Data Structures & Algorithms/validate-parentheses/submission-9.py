class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {")":"(","}":"{","]":"[",}

        stack = []

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack or (pairs[char] != stack[-1]):
                    return False
                stack.pop()

        
        return not stack




        