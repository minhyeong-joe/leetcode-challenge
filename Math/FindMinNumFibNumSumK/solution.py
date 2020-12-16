def fib(upper):
    """
    Find the fibonacci numbers up to upper (inclusive)
    Instead of using recursion, use Memoization.
    """
    if upper < 1:
        return []
    fibNums = [1, 1]
    while fibNums[-2] + fibNums[-1] <= upper:
        fibNums.append(fibNums[-2]+fibNums[-1])
    return fibNums


def findMinFibonacciNumbers(k):
    """
    Given the number `k`, return the minimum number of Fibonacci numbers whose sum is equal to `k`, whether a Fibonacci number could be used multiple times.
    """
    fibNums = fib(k)
    numOfAdd = 0
    for i in range(len(fibNums)-1, -1, -1):
        # since a fib num can be used multiple times, use while instead of if
        while fibNums[i] <= k:
            numOfAdd += 1
            k -= fibNums[i]
    return numOfAdd



output = findMinFibonacciNumbers(7)
print("Input: k = 7")
print("Output:", output)

output = findMinFibonacciNumbers(10)
print("Input: k = 10")
print("Output:", output)

output = findMinFibonacciNumbers(19)
print("Input: k = 19")
print("Output:", output)

output = findMinFibonacciNumbers(5)
print("Input: k = 5")
print("Output:", output)

output = findMinFibonacciNumbers(1)
print("Input: k = 1")
print("Output:", output)

