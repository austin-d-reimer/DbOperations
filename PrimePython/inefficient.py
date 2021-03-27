class PrimePy:
    number_table = []
    primeNumbers = [1, 2]
    maxNum = 1000
    rawbits = None

    def __init__(self, maxNum):
        self.maxNum = maxNum
        self.rawbits = [True] * (int((self.maxNum + 1) / 2))

    def reset(self):
        self.number_table = list(range(3, self.maxNum + 1, 2))
        self.primeNumbers = [1, 2]

    def my_version(self):
        while len(self.number_table) > 1:
            self.primeNumbers.append(self.number_table[0])
            self.my_remove_set(self.number_table[0])

    def my_remove_set(self, inputNum):
        self.number_table = [
            (item) for item in self.number_table if item % inputNum != 0
        ]

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
