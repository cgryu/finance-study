import numpy as np
rng = np.random.default_rng(123)

# Exercise 1 - Binomial Verification
trials = 100000
results = rng.binomial(10, 0.5, trials)
distribution = np.bincount(results)
for i in range(len(distribution)):
    print(f"{i}s: {distribution[i]}")

average = np.average(results)
variance = np.var(results)

print(f"Simulation Average: {average}")
print(f"Simulation Variance: {variance}")

calcAverage = 10 * 0.5
calcVariance = (10 * 0.5) * 0.5

print(f"Calculated Average: {calcAverage}")
print(f"Calculated Variance: {calcVariance}")

# Exercise 2 - Geometric Verification
trials = 100000
results = rng.geometric((1/6), trials)
distribution = np.bincount(results)
for i in range(len(distribution)):
    print(f"{i}s: {distribution[i]}")

average = np.average(results)
variance = np.var(results)

print(f"Simulation Average: {average}")
print(f"Simulation Variance: {variance}")

calcAverage = 1/(1/6)
calcVariance = (1-(1/6)) / ((1/6) ** 2)

print(f"Calculated Average: {calcAverage}")
print(f"Calculated Variance: {calcVariance}")

# Exercise 3 - Variance of Linear Transformations
trials = 100000
simResultsX = rng.binomial(16, 0.5, trials)
simResultsY = rng.binomial(36, 0.5, trials)

simResultsZ = 2 * simResultsX - 3 * simResultsY

calcVariance = 97
simVariance = np.var(simResultsZ)

print(f"Calculated Variance: {calcVariance}")
print(f"Simulated Variance: {simVariance:.4f}")

# Exercise 4 - Multi-day Stock Return
trials = 100000
dayReturn = rng.normal(0.001, 0.015, trials * 5)
dayReturn = dayReturn.reshape(-1, 5)

fiveDayReturn = np.sum(dayReturn, axis=1)

simAverage = np.average(fiveDayReturn)
simVariance = np.var(fiveDayReturn)

print(f"Simulated Average: {simAverage:.4f}")
print(f"Simulated Variance: {simVariance}")