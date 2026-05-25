import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)
returns = rng.normal(loc=0.0008, scale=0.018, size=252)

print(f"""
Sample Mean: {returns.mean()}
Sample Standard Deviation: {returns.std()}
Skew: {stats.skew(returns)}
Kurtosis: {stats.kurtosis(returns)}
""")

mu, sigma = stats.norm.fit(returns)

x = np.linspace(returns.min(), returns.max(), 100)

var95 = stats.norm.ppf(0.05, loc=mu, scale=sigma)
var95Emp = np.percentile(returns, 5)
var99 = stats.norm.ppf(0.01, loc=mu, scale=sigma)
var99Emp = np.percentile(returns, 1)

print(f"""
FND VaR 95%: {var95:.4f}
Empirical VaR 95%: {var95Emp:.4f}
FND VaR 99%: {var99:.4f}
Empirical VaR 99%: {var99Emp:.4f}
""")

plt.hist(returns, bins=50, density=True, label="Daily Returns")
plt.plot(x, stats.norm.pdf(x, mu, sigma), color='red', label = "Fitted Normal PDF")
plt.title("Histogram of Daily Returns")
plt.xlabel("Returns")
plt.ylabel("Density")
plt.axvline(x=var95, color='red', linestyle='--', label='VaR 95%')
plt.axvline(x=var99, color='red', label='VaR 99%')

plt.legend()

plt.show()

# Extension
tdist = stats.t.rvs(df=4, loc=0.0008, scale=0.018, size=252)
var95t = np.percentile(tdist, 5)
var99t = np.percentile(tdist, 1)
print(f"T-Distribution VaR 95%: {var95t:.4f}")
print(f"T-Distribution VaR 99%: {var99t:.4f}")

