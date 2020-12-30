def divisible(s: str, t: str) -> int:
    # this edge case catch is optional because of problem constraints
    if len(s) < len(t) or len(s) == 0 or len(t) == 0:
        return -1
    # if length is not divisible
    if len(s) % len(t) != 0:
        return -1
    # find smallest common string of two
    # bcdbcdbcdbcd[1:-1] -> cdbcdbcdbc.find(bcdbcd) -> 2
    i = (t+t)[1:-1].find(t)
    smallestString = t[i+1:]    # bcdbcd[3:] -> bcd
    # print(smallestString)
    # check if s is also repeating smallest string
    while len(t) < len(s):
        t += t
        if s == t:
            return len(smallestString)
        else:
            return -1


s = "bcdbcdbcdbcd"
t = "bcdbcd"
print(divisible(s, t))
