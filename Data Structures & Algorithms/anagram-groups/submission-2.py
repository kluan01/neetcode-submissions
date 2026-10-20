class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # { freq : [str1, str2] }
        freqToStrs = defaultdict(list)

        for s in strs:
            sFreq = [0] * 26
            for c in s:
                sFreq[ord(c) - ord('a')] += 1

            freqToStrs[tuple(sFreq)].append(s)

        return list(freqToStrs.values())
    