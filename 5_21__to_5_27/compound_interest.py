principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate in %: "))/100
years = int(input("Enter the amount of time in years: "))

def get_future_value(principal1, rate1, years1):
    return principal1 * (1+rate1) ** years1

future_value = get_future_value(principal, rate, years)
print(f"Starting amount: ${principal}")
print(f"After {years} years at {rate*100:.1f}% interest you earned: ${future_value:.2f}")
print(f"Total profit: ${future_value - principal:.2f}")

for n in range(1, years+1):
    future_val = get_future_value(principal, rate, n)
    print(f"The future value after year {n} is ${future_val:.2f} and the interest earned is ${future_val - principal:.2f}")