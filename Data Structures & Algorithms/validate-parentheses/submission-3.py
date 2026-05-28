class Solution:
    def isValid(self, s: str) -> bool:
        # map of valid paren
        valid = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        # stack to track paren
        stack = []
        # loop through s:
        for c in s:
            # if closing brack - check open stack == stack.pop
            if c in valid:
                if stack and stack[-1] == valid[c]:
                    stack.pop()
                # if false return
                else:
                    return False
            
            else:# add to stack
                stack.append(c)

        # return true
        return True if not stack else False
        