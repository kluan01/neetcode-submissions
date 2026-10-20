class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [ [], [], [] ]
        freqList = [ [] for _ in range(len(nums) + 1) ]

        # { int : count }
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for num, cnt in count.items():
            freqList[cnt].append(num)

        res = []
        for i in range(len(freqList) - 1, 0, -1):
            for num in freqList[i]:
                res.append(num)
                if len(res) == k: 
                    return res