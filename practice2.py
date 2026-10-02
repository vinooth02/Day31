import numpy as np

def countEvenOdd(numbers):

    evenCount = np.sum(numbers % 2 == 0)
    oddCount = np.sum(numbers % 2 != 0)

    return evenCount, oddCount


def startProgram():

    numbers = np.array([10, 21, 32, 45, 50, 63])

    evenCount, oddCount = countEvenOdd(numbers)

    print("Numbers:", numbers)
    print("Even:", evenCount)
    print("Odd:", oddCount)


startProgram()