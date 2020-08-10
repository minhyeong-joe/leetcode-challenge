def print2D(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print()


def countSubstrings(s: str) -> int:
    # initialize NxN dynamic programming table
    dpTable = [[False for i in range(len(s))] for j in range(len(s))]
    count = 0
    # bottom-up fill in dynamic table
    # True if substring[i:j+1] is a palindrome
    # always True for length 1
    # always False when j < i
    # when length = 2, true if s[i] is same as s[j]
    # for any others, True iff s[i] == s[j] and dpTable[i+1][j-1] is also True
    for i in range(len(s)-1, -1, -1):
        for j in range(len(s)-1, -1, -1):
            if i == j:
                dpTable[i][j] = True
                count += 1
            elif i > j:
                dpTable[i][j] = False
            elif i+1 == j and s[i] == s[j]:
                dpTable[i][j] = True
                count += 1
            elif s[i] == s[j] and dpTable[i+1][j-1]:
                dpTable[i][j] = True
                count += 1
    print2D(dpTable)

    return count


# test driver
input = "abc"
print("Input:", input)
print("Output:", countSubstrings(input))
print()

input = "aaa"
print("Input:", input)
print("Output:", countSubstrings(input))
print()

input = "aababba"
print("Input:", input)
print("Output:", countSubstrings(input))
print()
