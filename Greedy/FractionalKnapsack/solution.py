from collections import defaultdict


def fractionalKnapsack(weights, values, capacity):
    maxValue = 0
    unitValues = defaultdict(int)
    for i in range(len(weights)):
        unitValues[values[i]/weights[i]] += weights[i]
    while capacity:
        valueToAdd = max(unitValues)
        weightToAdd = min(capacity, unitValues[valueToAdd])
        maxValue += valueToAdd * weightToAdd
        unitValues[valueToAdd] -= weightToAdd
        if unitValues[valueToAdd] == 0:
            del unitValues[valueToAdd]
        capacity -= weightToAdd
    return maxValue


weights = [2, 1, 3]
values = [10, 6, 12]
capacity = 5
print(fractionalKnapsack(weights, values, capacity))
