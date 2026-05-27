import numpy as np 
import pandas as pd

rng = np.random.default_rng(seed=42)

dates = pd.date_range(start="2023-01-02", periods = 252, freq='B')
price_data = {
    "AAPL": 100 * np.cumprod(1 + rng.normal(0.0005, 0.018, 252)),
    "MSFT": 100 * np.cumprod(1 + rng.normal(0.0004, 0.015, 252)),
    "JPM": 100 * np.cumprod(1 + rng.normal(0.0003, 0.012, 252))
}

prices = pd.DataFrame(price_data, index=dates)

# Task 1
print(f"Head:\n {prices.head()}")

# Task 2
print(f"Tail:\n {prices.tail()}")

# Task 3
print(f"Shape: {prices.shape}")

# Task 4
aapl = prices["AAPL"]
print(f"AAPL type: {type(aapl)}") # SERIES, not dataframe

# Task 5
march2023 = prices.loc["2023-03"]
print(f"First 3 rows:\n {march2023.head(3)}")

# Task 6
returns = prices.pct_change()
returns = returns.dropna()

print(f"Returns first 3 rows:\n {returns.head(3)}")

# Task 7
aaplAverage = returns["AAPL"].mean()
msftAverage = returns["MSFT"].mean()
jpmAverage = returns["JPM"].mean()

print(f""" Mean Daily Return per Stock
AAPL: {aaplAverage:.4f}
MSFT: {msftAverage:.4f}
jpmAverage: {jpmAverage:.4f}
""")

# Task 8
aaplSTD = returns["AAPL"].std()
msftSTD = returns["MSFT"].std()
jpmSTD = returns["JPM"].std()

print(f""" Standard Deviation of Daily Return per Stock
AAPL: {aaplSTD:.4f}
MSFT: {msftSTD:.4f}
jpmAverage: {jpmSTD:.4f}
""")

# Task 9
worstReturn = returns.min().min()
print(f"Worst Return: {worstReturn:.4f}")

# Task 10
prices["Portfolio"] = prices[["AAPL", "MSFT", "JPM"]].mean(axis=1)
print(f"First 5 rows:\n {prices.head()}")