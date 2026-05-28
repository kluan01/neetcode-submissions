class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        # iterate through strings
        for s in strs:        
            # create delimeter & append
            count = len(s)
            result += (str(count) + "#" + s)
        
        # return str
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        # iterate through string
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            count = int(s[i:j])
            i = j + 1
            j = i + count
            result.append(s[i:j])
            i = j
        
        # return list
        return result
