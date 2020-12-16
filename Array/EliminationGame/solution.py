def lastRemaining(n: int) -> int:
    if n == 1:
        return n
    leftToRight = True
    step = 1
    survivor = 2
    
    while n > 1:
        # eliminate half of n's
        n = n // 2
        step = step * 2
        # if at this point, n has one survivor, return it
        if n == 1:
            return survivor
        # direction changes every iteration (starting with left-to-right)
        leftToRight = not leftToRight
        if leftToRight or (not leftToRight and n % 2 == 1):
            survivor += step
    return survivor
        

# test driver
input = 9
print("Input: n =", input)
print("Output:", lastRemaining(9))