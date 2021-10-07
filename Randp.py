# gives non-repeating random numbers. Built in CS Capstone.
import math
import random


class Randp:
    def __init__(self, number_of_digits):
        self.nums = [i + 1 for i in range(number_of_digits)]
        self.numsLeft = number_of_digits

    def next_int(self):
        if self.numsLeft == 0:
            return 0
        index = math.floor(random.random()*self.numsLeft)
        num = self.nums[index]
        self.nums[index] = self.nums[self.numsLeft - 1]
        self.nums[self.numsLeft - 1] = num
        self.numsLeft -= 1
        return num #self.nums.pop(index)

if __name__ == "__main__":

    r = Randp(5)
    for i in range(6):
        print(r.next_int())