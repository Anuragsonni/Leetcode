class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = set()
        stack = []
        leftr, rightr = 0, 0
        for i in s :
            if i == '(':
                leftr+=1
            elif i==')':
                if leftr:
                    leftr-=1
                else:
                    rightr+=1
        def backtrack (idx, curr, left , right, leftr, rightr):
            if idx == len(s) :
                if leftr==0 and rightr==0:
                        result.add("".join(curr))
                return

            if s[idx] == '(':
                # remove it
                if leftr:
                    backtrack(idx+1, curr.copy(), left, right, leftr-1, rightr)
                # take it
                backtrack(idx+1, curr + ['('], left+1, right, leftr, rightr)
            elif s[idx] == ')':
                # remove it
                if rightr:
                    backtrack(idx+1, curr.copy(), left, right, leftr, rightr-1)
                # take it
                if left > right:
                    backtrack(idx+1, curr + [')'], left, right+1, leftr, rightr)
            else:
                backtrack(idx+1, curr + [s[idx]], left, right, leftr, rightr)

        backtrack(0, [], 0, 0, leftr, rightr)
        return list(result) 