import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

rng = np.random.default_rng(seed=42)

n_days = 252
returns_data = pd.DataFrame({
    "AAPL": rng.normal(0.0005, 0.018, n_days),
    "MSFT": rng.normal(0.0004, 0.015, n_days),
    "JPM": rng.normal(0.0003, 0.012, n_days)
})

mean_returns = returns_data.mean() * 252
cov_matrix = returns_data.cov() * 252

def portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate=0.04):
    port_return = np.dot(weights, mean_returns)
    port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe = (port_return - risk_free_rate) / port_vol
    return port_return, port_vol, sharpe

# Part 1
equal_weights = np.array([1/3,1/3,1/3])
eq_return, eq_vol, eq_sharpe = portfolio_performance(equal_weights, mean_returns, cov_matrix)
print(f"""Results of equal weight simulation
Return: {eq_return}
Volatility: {eq_vol}
Sharpe Ratio: {eq_sharpe}
""")

# Part 2
def neg_sharpe(weights, mean_returns, cov_matrix, risk_free_rate=0.04):
    return -portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate)[2]

n_assets = len(mean_returns)
constraints = {"type":"eq", "fun": lambda w: np.sum(w) - 1}
bounds = tuple((0,1) for _ in range(n_assets))
x0 = np.array([1/n_assets]*n_assets)

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

# Step 3
def portfol_var(weights, mean_returns, cov_matrix, risk_free_rate=0.04):
    return (portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate)[1])**2

opt_result_var = minimize(portfol_var, x0,
                          args=(mean_returns, cov_matrix),
                          method="SLSQP",
                          bounds=bounds,
                          constraints=constraints)

opt_weights_var = opt_result_var.x
opt_ret_var, opt_vol_var, opt_sharpe_var = portfolio_performance(opt_weights_var, mean_returns, cov_matrix)

weight_dict_var = dict(zip(returns_data.columns, opt_weights_var.round(4)))

print(f"\nOptimal Weights: {weight_dict_var}")
print(f"Optimal Return:     {opt_ret_var:.4f}")
print(f"Optimal Volatility: {opt_vol_var:.4f}")
print(f"Optimal Sharpe:     {opt_sharpe_var:.4f}")

# Step 4
tableData = np.zeros(9)
tableData = tableData.reshape(3,3)
tableData[:0] = eq_return, eq_vol, eq_sharpe
tableData[:1] = opt_ret, opt_vol, opt_sharpe
tableData[:2] = opt_ret_var, opt_vol_var, opt_sharpe_var

compTable = pd.DataFrame(tableData,
                         index=["Equal Weight", "Max Sharpe", "Min Variance"],
                         columns=["Return", "Volatility", "Sharpe"])

# Step 5
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

plt.scatter(results[1], results[0], c=results[2], cmap="viridis",
            alpha=0.5, s=10, label="Random Portfolios")
plt.colorbar(label="Sharpe Ratio")

plt.xlabel("Annualized Volatility (σ)")
plt.ylabel("Annualized Return")
plt.title("Efficient Frontier — Monte Carlo Simulation")

plt.scatter(opt_vol, opt_ret, color="red", marker="*", s=300, label="Max Sharpe Portfolio")
plt.scatter(eq_vol, eq_return, color="orange", marker="*", s=300, label="Equal Weights Portfolio")
plt.scatter(opt_vol_var, opt_ret_var, color="brown", marker="*", s=300, label="Min Variance Portfolio")

cml_x = np.linspace(0, opt_vol * 1.5, 100)
cml_y = 0.04 + (opt_sharpe * cml_x)
plt.plot(cml_x, cml_y, color='green', linewidth=1.5, linestyle='--', label='Capital Market Line')
plt.legend()
plt.show()