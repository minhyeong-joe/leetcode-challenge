def substrKDistinctChars(s, k):
    # result = list()
    result = 0
    for i in range(len(s)):
        distinctChars = set({s[i]})
        # subString = s[i]
        for j in range(i+1, len(s)):
            if len(distinctChars) < k or (len(distinctChars) == k and s[j] in distinctChars):
                distinctChars.add(s[j])
                # subString += s[j]
            else:
                break
            if len(distinctChars) == k:
                # result.append(subString)
                result += 1
    return result


# test case
s = "pqpqs"
k = 2
print(substrKDistinctChars(s, k))
