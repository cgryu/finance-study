import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)

dates = pd.date_range(start="2023-01-02", periods = 252, freq='B')
price_data = {
    "AAPL": 100 * np.cumprod(1 + rng.normal(0.0005, 0.018, 252)),
    "MSFT": 100 * np.cumprod(1 + rng.normal(0.0004, 0.015, 252)),
    "JPM": 100 * np.cumprod(1 + rng.normal(0.0003, 0.012, 252))
}

prices = pd.DataFrame(price_data, index=dates)

returns = prices.pct_change().dropna()

# Part 1
cols = ["AAPL", "MSFT", "JPM"]
averages = returns[cols].mean()
stdev = returns[cols].std()
annualstd = stdev * np.sqrt(252)
var95aapl = np.percentile(returns["AAPL"], 5)
var95msft = np.percentile(returns["MSFT"], 5)
var95jpm = np.percentile(returns["JPM"], 5)

print(f"Average of each Stock:\n{averages}")
print(f"Standard Deviation of Daily Returns:\n{stdev}")
print(f"Annualized Standard Deviation:\n{annualstd}")
print(f"Empirical 95% VaR AAPL:\n{var95aapl}")
print(f"Empirical 95% VaR MSFT:\n{var95msft}")
print(f"Empirical 95% VaR JPM:\n{var95jpm}")

# Part 2
print(returns.corr())

# Part 3
port_returns = returns.mean(axis=1)
port_mean = port_returns.mean()
port_sig = port_returns.std()
port_asig = port_sig * np.sqrt(252)
portvar95 = np.percentile(port_returns, 5)

print(f"Average of Portfolio Returns:\n{port_mean}")
print(f"Portfolio Standard Deviation:\n{port_sig}")
print(f"Portfolio Annualized Standard Deviation:\n{port_asig}")
print(f"Portfolio Empirical 95% VaR:\n{portvar95}")

print(f"""
Average Individual Sigma: {stdev.mean()}
Portfolio Sigma: {port_sig}
""")

# Part 4
cumulative = (1 + returns).cumprod() - 1
port_cumulative = (1 + port_returns).cumprod() - 1

for col in cumulative.columns:
    plt.plot(cumulative.index, cumulative[col], label=col)

plt.plot(port_cumulative.index, port_cumulative, label="Portfolio", linestyle='--', color='red')

plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.title('Cumulative Returns of Stock vs Portfolio')
plt.legend()
plt.show()

# Extension
var99aapl = np.percentile(returns["AAPL"], 1)
var99msft = np.percentile(returns["MSFT"], 1)
var99jpm = np.percentile(returns["JPM"], 1)
portvar99 = np.percentile(port_returns, 1)

var_table = pd.DataFrame({
    "VaR 95%": [var95aapl, var95msft, var95jpm, portvar95],
    "VaR 99%": [var99aapl, var99msft, var99jpm, portvar99]
}, index = ["AAPL", "MSFT", "JPM", "Portfolio"])

print(var_table)
