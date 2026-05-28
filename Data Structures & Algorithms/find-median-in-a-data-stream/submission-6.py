class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array.sort()

    def findMedian(self) -> float:
        arrLen = len(self.array)
        middle = arrLen // 2
        if arrLen % 2 == 0:
            return (self.array[middle - 1] + self.array[middle]) / 2
        
        return self.array[middle]
        
        