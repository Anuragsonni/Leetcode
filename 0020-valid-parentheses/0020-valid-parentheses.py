class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            ')' : '(',
            ']' : '[', 
            '}' : '{'
        }
        stack = []
        for i in s :
            if i in bracket :
                top=stack.pop() if stack else '#'
                if bracket[i] != top:
                    return False
            
            else:
                stack.append(i)

        return True if not stack else False