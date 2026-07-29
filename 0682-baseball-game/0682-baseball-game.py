class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(2*stack[-1])
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        
        return sum(stack)
        # stack = []
        # for i in operations:
        #     if i == "C":
        #         stack.pop()
        #     elif i == "D":
        #         top = stack.pop()
        #         stack.extend([top, 2*top])
        #     elif i == "+":
        #         b = stack.pop()
        #         a = stack.pop()
        #         stack.extend([a, b, a+b])
        #     else:
        #         stack.append(int(i))
        
        # return sum(stack)
