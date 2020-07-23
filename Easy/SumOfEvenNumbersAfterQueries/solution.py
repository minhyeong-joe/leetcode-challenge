def sumEvenAfterQueries(A, queries):
    answer = list()
    for q in queries:
        A[q[1]] += q[0]
        sumOfEvens = 0
        for num in A:
            if num % 2 == 0:
                sumOfEvens += num
        answer.append(sumOfEvens)
    return answer


# test driver
A = [1, 2, 3, 4]
queries = [[1,0], [-3,1], [-4,0], [2,3]]

print(sumEvenAfterQueries(A, queries))