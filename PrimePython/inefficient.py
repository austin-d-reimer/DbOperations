import timeit
import numpy as np


class PrimePy:
    number_table = []
    primeNumbers = [1, 2]
    maxNum = None
    start = True
    tStart = None

    def __init__(self, maxNum):
        self.maxNum = maxNum

    def reset(self):
        self.number_table = np.arange(3, self.maxNum + 1, 2).tolist()
        self.primeNumbers = [1, 2]

    def run(self):
        while len(self.number_table) > 1:
            self.primeNumbers.append(self.number_table[0])
            self.remove_set(self.number_table[0])

    def remove_set(self, inputNum):
        self.number_table = [
            (item) for item in self.number_table if item % inputNum != 0
        ]

    def run_test(self):
        while len(self.number_table) > 1:
            self.primeNumbers.append(self.number_table[0])
            self.remove_test(self.number_table[0])

    def remove_test(self, inputNum):
        print(self.number_table[0:20])
        self.number_table = [
            (item) for item in self.number_table if item % inputNum != 0
        ]

    def timeResults(self):

        if self.start:
            pp.reset()
            print("Starting Test")
            self.tStart = timeit.default_timer()
            self.start = False
        else:
            self.start = True
            return timeit.default_timer() - self.tStart

    def validate(self):
        primeCounts = {
            1_000: 168,
            10_000: 1_229,
            100_000: 9_592,
            1_000_000: 78_498,
            10_000_000: 664_579,
            100_000_000: 5_761_455,
        }
        return len(self.primeNumbers) == primeCounts[self.maxNum]

    # def remove_even(self):
    #     return self.number_table[0:-1:2]
    # def slow_code1_run(self):
    #     self.reset()
    #     self.number_table = self.remove_even()

    #     while len(self.number_table) > 1:
    #         self.primeNumbers.append(self.number_table[0])

    #         self.remove_set(self.number_table[0])

    # def slow_code1_remove_set(self, inputNum):
    #     newList = []
    #     for number in self.number_table:
    #         if number % inputNum != 0:
    #             newList.append(number)
    #     self.number_table = newList

    # def run(self):
    #     self.number_table = list(range(3, self.maxNum + 1, 2))
    #     while len(self.number_table) > 1:
    #         self.primeNumbers.append(self.number_table[0])
    #         self.remove_set(self.number_table[0])

    # def remove_set(self, inputNum):
    #     tempList = self.number_table
    #     count = 0
    #     for listItem in tempList:
    #         if listItem % inputNum == 0:
    #             self.number_table.pop(count)
    #         count += 1


pp = PrimePy(1_000)
passes = 0

pp.timeResults()
result = pp.run()
time = pp.timeResults()
print(len(pp.primeNumbers))
print(f"Got result in {time}seconds and it was {pp.validate()}.")


pp.timeResults()
pp.run_test()
time = pp.timeResults()
print(f"Got result in {time}seconds and it was {pp.validate()}.")
