from math import sqrt


class Eulers:
    maxNum = 1000
    rawbits = []

    def __init__(self, maxNum):
        self.rawbits = [False] + [True] * (int((maxNum + 1) / 2))
        self.maxNum = maxNum

    def reset(self):
        self.rawbits = [False] + [True] * (int((self.maxNum + 1) / 2))

    def run(self):
        facter = 3
        q = sqrt(self.maxNum)

        while facter < q:
            for num in range(facter, self.maxNum):
                if self.get_odd(num):
                    facter = num
                    break

            for num in range(facter * 3, self.maxNum, facter * 2):
                self.change_bit(num)
            facter += 2

    def countPrimes(self):
        count = 0
        for bit in self.rawbits:
            if bit:
                count += 1
        return count

    def get_odd(self, number):
        if number % 2 == 0:
            return False
        else:
            return self.rawbits[int(number / 2)]

    def change_bit(self, index):
        self.rawbits[int(index / 2)] = False