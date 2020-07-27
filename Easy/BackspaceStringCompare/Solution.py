from itertools import zip_longest

def backspaceCompare(S: str, T: str) -> bool:
    sStack = list()
    tStack = list()
    # add characters into each stack, pop if it sees backspace '#'.
    for ch in S:
        if ch == '#':
            if sStack:
                sStack.pop()
        else:
            sStack.append(ch)
    for ch in T:
        if ch == '#':
            if tStack:
                tStack.pop()
        else:
            tStack.append(ch)
    return sStack == tStack


# this is a very smart solution from Leetcode
# It uses O(1) space
# general idea is to iterate from back to see the backspace '#' beforehand, so we know which characters to ignore (as it is "deleted" by backspace)
# use `all(x == y for x, y in itertools.zip_longest(ITERABLE, ITERABLE))` to compare every generated values are equal.
def backspaceCompareSmart(S: str, T: str) -> bool:
    return all(x == y for x,y in zip_longest(buildString(S), buildString(T)))


# instead of creating a string, "yield" returns generated iterable (one-time use and forgotten)
def buildString(S: str):
    skip = 0
    for ch in reversed(S):
        if ch == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            yield ch


# Test Driver
S = "ab#c"
T = "ad#c"
print("Input: S = \"" + S + "\", T = \"" + T + "\"")
print("Output:", backspaceCompare(S, T))

S = "ab##"
T = "c#d#"
print("Input: S = \"" + S + "\", T = \"" + T + "\"")
print("Output:", backspaceCompare(S, T))

S = "a##c"
T = "#a#c"
print("Input: S = \"" + S + "\", T = \"" + T + "\"")
print("Output:", backspaceCompare(S, T))

S = "a#c"
T = "b"
print("Input: S = \"" + S + "\", T = \"" + T + "\"")
print("Output:", backspaceCompare(S, T))

# solution way test
S = "ab#c"
T = "ad#c"
print("Input: S = \"" + S + "\", T = \"" + T + "\"")
print("Output:", backspaceCompareSmart(S, T))

S = "a#c"
T = "b"
print("Input: S = \"" + S + "\", T = \"" + T + "\"")
print("Output:", backspaceCompareSmart(S, T))