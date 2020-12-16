def minAddToMakeValid(S):
    stack = list()
    minAdd = 0
    for paren in S:
        if paren == '(':
            stack.append(paren)
        else:
            try:
                stack.pop()
            except IndexError as e:
                minAdd += 1
    minAdd += len(stack)
    return minAdd

input = "())"
print(input)
print(minAddToMakeValid(input))

input = "((("
print(input)
print(minAddToMakeValid(input))

input = "()"
print(input)
print(minAddToMakeValid(input))

input = "()))(("
print(input)
print(minAddToMakeValid(input))

input = "))((()())"
print(input)
print(minAddToMakeValid(input))