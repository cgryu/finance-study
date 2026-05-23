import numpy as np
rng = np.random.default_rng(1)

# Simulation 1
a = rng.integers(1, 7, 100000)
count = np.count_nonzero(a > 4)

print(f"The proportion of rolls from the simulation was {(count/100000):.4f}.")
print("The analytical answer was 0.3333.")

# Simulation 2
dice1 = rng.integers(1,7,100000)
dice2 = rng.integers(1,7,100000)
diceSum = dice1 + dice2

count = np.count_nonzero(diceSum == 7)
print(f"The proportion of rolls from the simulation was {(count/100000):.4f}")
print(f"The analytical answer was {(1/6):.4f}.")

# Simulation 3
a = rng.integers(1,7,300000)
a = a.reshape(-1, 3)

count = 0
for row in a:
    if np.any(row == 6):
        count += 1
print(f"The proportion of rolls from the simulation was {count/100000:.4f}")
print(f"The analytical answer was {(91/216):.4f}")

# Simulation 4
deck = np.arange(1,53)
trials = 100000
count = 0

for _ in range(trials):
    draw = rng.choice(deck, size = 2, replace=False)
    if draw[0] < 5 and draw[1] < 5:
        count += 1

count2 = 0
for _ in range(trials):
    draw = rng.choice(deck, size = 2, replace=True)
    if draw[0] < 5 and draw[1] < 5:
        count2 += 1

print(f"The proportion of rolls from the simulation with replacement was {(count2/100000):.4f}")
print(f"The analytical answer was {(1/169):.4f}.")

print(f"The proportion of rolls from the simulation without replacement was {(count/100000):.4f}")
print(f"The analytical answer was {(1/(13*17)):.4f}.")