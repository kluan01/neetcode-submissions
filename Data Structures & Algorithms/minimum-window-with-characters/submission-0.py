class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # length edge case
        if len(s) < len(t): return ""

        # 2 ptrs w/ freq arrayS
        countT, window = {}, {}

        # preload one freq array
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have and need variables
        have, need = 0, len(countT)
        # res by index, resLen by floatinf
        res, resLen = [-1, -1], float("infinity")

        l = 0

        # for loop to len(s)
        for r in range(len(s)):
            c = s[r]
            # add char to other freq array
            window[c] = 1 + window.get(c, 0)
            # if char is in orig freq arr + freqs are th esame
            if c in countT and countT[c] == window[c]:
                # inc have
                have += 1
            
            # while have = need
            while have == need:
                # if window len < resLen
                if (r - l + 1) < resLen:
                    # set vars
                    res = [l, r]
                    resLen = r - l + 1

                # decremenet window
                c = s[l]
                window[c] -= 1
                if c in countT and window[c] < countT[c]:
                    have -= 1
                # check freq arrays + maps
                l += 1

        # return shortest string
        if resLen == float("infinity"):
            return ""
        
        l, r = res
        return s[l : r + 1]
