class MyQueue(object):

    def __init__(self):
        self.enque = []
        self.deque = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.enque.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.deque:
            while self.enque:
                self.deque.append(self.enque.pop())
        return  self.deque.pop() 
        

    def peek(self):
        """
        :rtype: int
        """
        if self.deque:
            return self.deque[-1]
        while self.enque:
            self.deque.append(self.enque.pop())
        return self.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.deque or self.enque)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()