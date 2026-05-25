from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Normal Distribution
dist = stats.norm(loc=50, scale=10)
dist.pdf(60) # height of density curve at x = 60
dist.cdf(60) # P(X <= 60)
dist.ppf(0.95) # inverse CDF - value with 95% of distribution below it
dist.rvs(size=1000) # generate 1000 random samples

# Standard Normal
stats.norm.cdf(1.96) # should be 0.975

# Log-Normal
stats.lognorm(s=0.2, scale=np.exp(0.08))

# Exercise 1
print(f"Answer to question 1: {dist.cdf(60)}")

# Exercise 2
dist = stats.norm(loc=0.001, scale=0.015)
print(f"Answer to question 2: {dist.cdf(-0.02)}")

# Exercise 3
fifthPercentile = dist.ppf(0.05)
print(f"Answer to question 3: You will not exceed a loss of {fifthPercentile*100:.2f}% around 95% of the time.")

# Exercise 4
samples = dist.rvs(size=10000)
average = np.mean(samples)
stdev = np.std(samples)

print(f"""
Actual Average: 0.001
Actual Standard Deviation: 0.015
Calculated Average {average:.5f}
Calculated Standard Deviation: {stdev:.5f}
""")

# Exercise 5
plt.hist(samples, bins = 50, density=True, label="Samples")
plt.xlabel("Returns")
plt.ylabel("Density")
plt.title("Daily Returns Distribution")

x = np.linspace(samples.min(), samples.max(), 100)
plt.plot(x, stats.norm.pdf(x, 0.001, 0.015), color="red", label="Normal PDF")
plt.axvline(x=fifthPercentile, color='red', linestyle='--', label='VaR 95%')

plt.legend()

plt.show()

# Exercise 6
dist = stats.lognorm(s=0.2, scale=np.exp(0.08))
print(f"Mean: {dist.mean()}")
print(f"Median: {dist.median()}")