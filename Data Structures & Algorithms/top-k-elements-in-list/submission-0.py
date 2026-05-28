class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]
        seen = {}
        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        for key, value in seen.items():
            count[value].append(key)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
        