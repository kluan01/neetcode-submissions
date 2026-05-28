class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count, search = [0] * 26, [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            search[ord(t[i]) - ord('a')] += 1

        return count == search
        