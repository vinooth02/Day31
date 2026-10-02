import numpy as np

def findSecondLargest(numbers):

    uniqueNumbers = np.unique(numbers)

    sortedNumbers = np.sort(uniqueNumbers)

    return sortedNumbers[-2]


def startProgram():

    numbers = np.array([10, 25, 7, 40, 15])

    result = findSecondLargest(numbers)

    print("Numbers:", numbers)
    print("Second Largest:", result)


startProgram()