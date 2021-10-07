# silly little parking problem given in CS Capstone
import random


def gen_parking_lot(parking_spaces):
    parking = [0 for i in range(parking_spaces)]
    parked_cars = 0

    for i in range(parking_spaces):
        if random.randint(0, 1) == 1:
            parking[i] = 1
            parked_cars += 1
    return parked_cars


def avrg_park(accuracy, parking_spaces):
    curr_sum = 0
    for i in range(accuracy):
        curr_sum += gen_parking_lot(parking_spaces)
    average = curr_sum / accuracy
    return average


# print(avrg_park(10000, 10))


# paley solution
def park(n):
    if n < 1:  # not enough space
        return 0
    else:
        # choose a random place to put the car
        location = random.random() * (n - 1)
        return 1 + park(location) + park(n - location - 1)
print(park(10))

def avrg_park(accuracy, parking_spaces):
    curr_sum = 0
    for i in range(accuracy):
        curr_sum += park(parking_spaces)
    average = curr_sum / accuracy
    return average
print(avrg_park(10000, 10))
# def fact(n):
#     if n < 2:
#         return 1
#     else:
#         return n*fact(n-1)
#
#
# print(fact(5))
