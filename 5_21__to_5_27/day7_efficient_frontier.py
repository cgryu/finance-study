import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

rng = np.random.default_rng(seed=42)

# Step 1

n_days = 252
returns_data = pd.DataFrame({
    "AAPL": rng.normal(0.0005, 0.018, n_days),
    "MSFT": rng.normal(0.0004, 0.015, n_days),
    "JPM": rng.normal(0.0003, 0.012, n_days)
})

mean_returns = returns_data.mean() * 252
cov_matrix = returns_data.cov() * 252

print(f"Annualized Mean Returns:\n{mean_returns}")
print(f"Annualized Covariance MAtrix:\n{cov_matrix}")

# Step 2
def portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate=0.04):
    port_return = np.dot(weights, mean_returns)
    port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe = (port_return - risk_free_rate) / port_vol
    return port_return, port_vol, sharpe

# Step 3
n_portfolios = 5000
results = np.zeros((3, n_portfolios))
weights_record = []

for i in range(n_portfolios):
    w = rng.random(3)
    w /= w.sum()
    weights_record.append(w)
    ret, vol, sharpe = portfolio_performance(w, mean_returns, cov_matrix)
    results[0, i] = ret
    results[1, i] = vol
    results[2, i] = sharpe

print(f"Best Sharpe from simulation: {results[2].max():.4f}")

# Step 4
def neg_sharpe(weights, mean_returns, cov_matrix, risk_free_rate=0.04):
    return -portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate)[2]

n_assets = len(mean_returns)
constraints = {"type":"eq", "fun": lambda w: np.sum(w) - 1}
bounds = tuple((0,1) for _ in range(n_assets))
x0 = np.array([1/n_assets] * n_assets)

opt_result = minimize(neg_sharpe, x0, 
                      args=(mean_returns, cov_matrix),
                      method="SLSQP",
                      bounds=bounds,
                      constraints=constraints)

opt_weights = opt_result.x
opt_ret, opt_vol, opt_sharpe = portfolio_performance(opt_weights, mean_returns, cov_matrix)

weight_dict = dict(zip(returns_data.columns, opt_weights.round(4)))

print(f"\nOptimal Weights: {weight_dict}")
print(f"Optimal Return:     {opt_ret:.4f}")
print(f"Optimal Volatility: {opt_vol:.4f}")
print(f"Optimal Sharpe:     {opt_sharpe:.4f}")

# Step 5
plt.figure(figsize=(10, 6))
plt.scatter(results[1], results[0], c=results[2], cmap="viridis",
            alpha=0.5, s=10, label="Random Portfolios")
plt.colorbar(label="Sharpe Ratio")
plt.scatter(opt_vol, opt_ret, color="red", marker="*", s=300, label="Max Sharpe Portfolio")
plt.xlabel("Annualized Volatility (σ)")
plt.ylabel("Annualized Return")
plt.title("Efficient Frontier — Monte Carlo Simulation")

# Capital Market Line
cml_x = np.linspace(0, opt_vol * 1.5, 100)
cml_y = 0.04 + (opt_sharpe * cml_x)
plt.plot(cml_x, cml_y, color='green', linewidth=1.5, linestyle='--', label='Capital Market Line')
plt.legend()
plt.show()

