
def longestCommonPrefix(strs):
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    common = ""
    if len(strs) == 0:
        return common
    for i in range(len(strs[0])):
        prefix = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != prefix:
                return common
        common += prefix
    return common

input = ["flower", "flow", "flight"]
output = longestCommonPrefix(input)
print("Input:", input)
print("Output:", output)

input = ["dog", "racecar", "car"]
output = longestCommonPrefix(input)
print("Input:", input)
print("Output:", output)
