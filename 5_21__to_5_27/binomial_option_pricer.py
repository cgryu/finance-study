import numpy as np

rng = np.random.default_rng(8282)

# HARDCODED FOR NOW
s0 = 100      # starting stock price
strike = 105  # strike price
u = 1.10      # up factor
d = 0.9       # down factor
p = 0.6       # probability of up move
r = 0.05      # risk-free rate (discount rate)

# Analytical Calculations
stockUp = s0 * u
stockDown = s0 * d
payoffUp = max(stockUp - strike, 0)
payoffDown = max(stockDown - strike, 0)
expectPayoff = p * payoffUp + (1-p) * payoffDown
optionPrice = expectPayoff / (1+r)

# Monte Carlo
trials = 100000

rolls = rng.binomial(1, p, trials)

values = np.where(rolls == 1, payoffUp, payoffDown)

simAverage = np.average(values)
simOptionPrice = simAverage / (1+r)

# Output
print(f"""
Up price: ${stockUp} --- Down price: ${stockDown}
Payoff Up: ${payoffUp} --- Payoff Down: ${payoffDown}
Calculated Option Price: ${optionPrice}
Simulated Option Price: ${simOptionPrice}
""")