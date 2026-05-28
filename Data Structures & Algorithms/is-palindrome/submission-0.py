class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l, r pointers
        l, r = 0, len(s) - 1
        # while l < r:
        while l < r:
            # if val is alnum, continue
            while l < r and s[l].isalnum() == False:
                l += 1
            while l < r and s[r].isalnum() == False:
                r -= 1

            # compare chars and reject accordingly
            if s[l].lower() != s[r].lower():
                return False
            # continue iteration
            l += 1
            r -= 1

        # return true
        return True

        