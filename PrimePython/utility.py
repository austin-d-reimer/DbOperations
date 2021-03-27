import timeit


def timeResults(start_time=0):
    if start_time != 0:
        return timeit.default_timer() - start_time

    else:
        print("Starting Test")
        return timeit.default_timer()


def validate(maxNum, num):
    primeCounts = {
        100: 25,
        1_000: 168,
        10_000: 1_229,
        100_000: 9_592,
        1_000_000: 78_498,
        10_000_000: 664_579,
        100_000_000: 5_761_455,
    }
    if num == primeCounts[maxNum]:
        return "correct"
    else:
        return "incorrect"
