class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.data = [None]*k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.head += 1
            self.tail += 1
            self.data[0] = value
            return True
        elif not self.isFull():
            if self.tail != self.size - 1:
                self.tail += 1
                self.data[self.tail] = value
                return True
            else:
                self.tail = 0
                self.data[self.tail] = value
                return True
        else:
            return False


    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        elif self.head == self.tail:
            self.head, self.tail = -1, -1
            return True
        else:
            if self.head != self.size - 1:
                self.head += 1
                return True
            else:
                self.head = 0
                return True



    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.data[self.head]



    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.data[self.tail]



    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.head == -1 and self.tail == -1:
            return True
        else:
            return False


    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.head == ( self.tail + 1 ) % self.size:
            return True
        else:
            return False      

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
