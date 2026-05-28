class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        return None
        

    def findMedian(self) -> float:
        self.arr.sort()
        arrLen = len(self.arr)
        if arrLen % 2 == 1:
            return self.arr[(arrLen - 1) // 2]
        
        return (self.arr[(arrLen // 2) - 1] + self.arr[arrLen // 2]) / 2
        