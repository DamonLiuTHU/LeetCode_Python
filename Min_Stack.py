class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inner_stack = list()
        self.MIN = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.inner_stack) == 0:
            self.MIN = x

        self.inner_stack.append(x - self.MIN)

        if x < self.MIN:
            self.MIN = x

    def pop(self):
        """
        :rtype: void
        """
        if len(self.inner_stack) == 0:
            return
        val = self.inner_stack.pop()
        if val < 0:
            self.MIN -= val

    def top(self):
        """
        :rtype: int
        """
        return self.inner_stack[-1] + self.MIN if self.inner_stack[-1] > 0 else \
            self.MIN

    def getMin(self):
        """
        :rtype: int
        """
        return self.MIN


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.getMin())
print(obj.top())
param_3 = obj.top()
param_4 = obj.getMin()
