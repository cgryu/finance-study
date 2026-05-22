# Exercise 1
def getAverage(numList):
    count = 0
    total = 0
    for number in numList:
        total += number
        count += 1
    return total/count if count > 0 else 0

# Exercise 2
def isPrime(x):
    factorCount = 0
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            factorCount += 1
    return False if factorCount > 0 else True

# Exercise 3
def perYearList(principal, rate, years):
    currentAmount = principal
    returnList = []
    for i in range(1, years+1):
        currentAmount *= 1+rate
        returnList.append((i, currentAmount))
    return returnList

# Exercise 4
def get_npv(cashFlow, rate):
    initial = cashFlow[0]
    final = 0

    for i in range(1, len(cashFlow)):
        final += cashFlow[i] / (1+rate)**i
    
    return final + initial

# Exercise 5
def countAboveThreshold(inputList, threshold):
    count = 0
    for number in inputList:
        if number > threshold:
            count += 1

    return count

# Exercise 6
def findTargetYear(principal, rate, target):
    amount = principal
    year = 0

    while amount < target:
        amount *= 1 + rate
        year += 1
    
    return year