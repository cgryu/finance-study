import numpy as np

rng = np.random.default_rng(15)
trials = [10, 100, 1000, 10000, 100000]
trialAverage = {}
sides = 6

for i in trials:
    a = rng.integers(1,sides+1,i)
    trialAverage[i] = float(np.average(a))

for key,value in trialAverage.items():
    print(f"Number of Trials: {key} ----- Average: {value:.4f} ----- Distance from Mean: {abs(((sides+1)/2)-value):.4f}")