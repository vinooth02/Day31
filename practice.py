import numpy as np

def findLargest(numbers):
    return np.max(numbers)


def startProgram():

    numbers = np.array([10, 25, 7, 40, 15])

    result = findLargest(numbers)

    print("Numbers:", numbers)
    print("Largest:", result)


startProgram()