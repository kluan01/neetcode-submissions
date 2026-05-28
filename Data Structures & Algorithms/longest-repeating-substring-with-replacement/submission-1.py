class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # DS = Freq. Map
        count = {}
        # 2 pointers + count + maxfreq
        l, res, maxfreq = 0, 0, 0

        # while r doens't reach end:
        for r in range(len(s)):
            # add to freq map
            count[s[r]] = 1 + count.get(s[r], 0)
            # define max f
            maxfreq = max(maxfreq, count[s[r]])

            # if window - maxfreq > k:
            while (r - l + 1) - maxfreq > k:
                # shrink window
                count[s[l]] -= 1
                l += 1

            # find max count
            res = max(res, r - l + 1)

        # return count
        return res