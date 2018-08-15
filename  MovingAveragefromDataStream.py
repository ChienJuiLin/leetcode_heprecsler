class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.Size = size
        self.data = [None]*size
        self.head = -1
        self.tail = -1

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.data[0] = val
            return float(val)
        elif (self.tail+1) % self.Size != self.head:
            self.tail += 1
            self.data[self.tail] = val
            return float(sum(self.data[:self.tail+1]))/(self.tail-self.head+1)
        else:
            self.head = (self.head + 1) % self.Size
            self.tail = (self.tail + 1) % self.Size
            self.data[self.tail] = val
            return float(sum(self.data))/self.Size



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
