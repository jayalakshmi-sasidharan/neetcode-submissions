class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                
                stack.pop()     

            else:
                stack.append(char)

        return len(stack) == 0

        # stack = []

        # while "()" in s or "[]" in s or "{}" in s:
        #     s = s.replace("()", "")
        #     s = s.replace("{}", "")
        #     s = s.replace("[]", "")
        
        # return s == ""

