class MedianFinder:

    def __init__(self):
        self.lower, self.upper = [], []

    def addNum(self, num: int) -> None:
        if self.upper and num > self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -1 * num)

        if len(self.lower) > len(self.upper) + 1:
            val = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)
        if len(self.upper) > len(self.lower) + 1:
            val = -1 * heapq.heappop(self.upper)
            heapq.heappush(self.lower, val)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -1 * self.lower[0]
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
        else:
            return (-1 * self.lower[0] + self.upper[0]) / 2.0
        