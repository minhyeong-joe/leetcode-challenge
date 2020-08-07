from typing import List

def carPooling(trips: List[List[int]], capacity: int) -> bool:
    # sort the list by pick-up location
    trips.sort(key=lambda trip: trip[1])
    print(trips)
    # in car keeps track of drop location and num of passengers to be dropped in dict
    inCar = {}
    distance = trips[0][1]
    # loading and unloading people
    while trips or inCar:
        # there are passengers inCar that need to be dropped off at this location
        if inCar and inCar.get(distance, 0) > 0:
            capacity += inCar[distance]
            del inCar[distance]
        # there are people who need to be picked up at this location 
        while trips and distance == trips[0][1]:
            capacity -= trips[0][0]
            if capacity < 0:
                return False
            # insert/increment {drop-location: numPassengers} into dictionary
            if inCar.get(trips[0][2], 0) == 0:
                inCar[trips[0][2]] = trips[0][0]
            else:
                inCar[trips[0][2]] += trips[0][0]
            trips.pop(0)
        distance += 1
    return True




# test driver
# trips = [[2,1,5], [3,3,7]]
# capacity = 4
# print("Input: trips =", trips, ", capacity =", capacity)
# print("Output:", carPooling(trips, capacity))
# print()

# trips = [[2,1,5], [3,3,7]]
# capacity = 5
# print("Input: trips =", trips, ", capacity =", capacity)
# print("Output:", carPooling(trips, capacity))
# print()

# trips = [[2,1,5],[3,5,7]]
# capacity = 3
# print("Input: trips =", trips, ", capacity =", capacity)
# print("Output:", carPooling(trips, capacity))
# print()

# trips = [[3,2,7], [3,7,9], [8,3,9]]
# capacity = 11
# print("Input: trips =", trips, ", capacity =", capacity)
# print("Output:", carPooling(trips, capacity))
# print()

trips = [[5,4,7],[7,4,8],[4,1,8]]
capacity = 17
print("Input: trips =", trips, ", capacity =", capacity)
print("Output:", carPooling(trips, capacity))
print()