def sumEvenAfterQueries(A, queries):
    answer = list()
    # initial sum
    sum = 0
    for num in A:
        if num % 2 == 0:
            sum += num
    for q in queries:
        oldVal = A[q[1]]
        A[q[1]] = oldVal + q[0]
        newVal = A[q[1]]
        if oldVal % 2 == 0:
            sum -= oldVal
        if newVal % 2 == 0:
            sum += newVal
        answer.append(sum)

    return answer


# test driver
A = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]

print(sumEvenAfterQueries(A, queries))
