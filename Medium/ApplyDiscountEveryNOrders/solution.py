from typing import List

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.count = 0
        self.dc = discount/100
        self.prod = dict()
        for i in range(len(products)):
            self.prod[products[i]] = prices[i]
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0.0
        self.count += 1
        for i in range(len(product)):
            total += amount[i] * self.prod.get(product[i], 0)
        if self.n == self.count:
            # apply discount and reset count
            total -= total * self.dc
            self.count = 0
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)


def cashOperator(operations, args):
    """
    Optional function to use list of inputs as in the example
    """
    if operations[0] != "Cashier":
        return None
    output = [None]
    cashierArgs = args[0]
    cashier = Cashier(cashierArgs[0], cashierArgs[1], cashierArgs[2], cashierArgs[3])
    for i, op in enumerate(operations[1:]):
        if op == "getBill":
            total = cashier.getBill(args[i+1][0], args[i+1][1])
            output.append(total)
    return output


ops = ["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
args = [[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
print("Input")
print(ops)
print(args)
print("Output")
print(cashOperator(ops, args))