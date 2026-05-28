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
            if stack and c in valid:

                res = stack.pop()
                # if false return
                if res != valid[c]:
                    return False
            
            else:# add to stack
                stack.append(c)

        # return true
        return True if not stack else False
        