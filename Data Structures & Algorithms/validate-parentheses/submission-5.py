class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {}

        pairs[")"] = "("
        pairs["]"] = "["
        pairs["}"] = "{"

        if (len(s)) % 2 != 0:
            return False
            

        for char in s:
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
            

        return len(stack) == 0

        