class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        queue = list()
        for c in s:
            # reverse string on ')'
            if c == ')':
                top = stack.pop()
                while top != '(':
                    queue.append(top)
                    top = stack.pop()
                # insert reversed substr back into stack
                while queue:
                    stack.append(queue.pop(0))
            else:
                stack.append(c)
        return "".join(stack)


# test driver
sol = Solution()
# s = "(ed(et(oc))el)"
s = "a(bcdefghijkl(mno)p)q"
print("Input:", s)
print("Output:", sol.reverseParentheses(s))