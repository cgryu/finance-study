choice = 0

def horizontalLine():
    print("----------------------------------------------------------")

def displayMenu():
    horizontalLine()
    print("""
    Please select an option
    (1) Future Value
    (2) Present Value
    (3) Annuity PV
    (4) NPV
    (5) Quit
    """)
    horizontalLine()

def FV_calculator(principal, rate, time):
    fv = principal * (1+rate) ** time
    return fv

def PV_calculator(FV, rate, time):
    pv = FV / (1+rate) ** time
    return pv

def annuityChoice():
    horizontalLine()
    annuityNumber = int(input("""
(1) Ordinary Annuity
(2) Annuity Due
(3) Perpetuity
"""))
    match annuityNumber:
        case 1:
            payment = float(input("Please enter the payment per period: "))
            rate = float(input("Please enter the rate: "))
            time = int(input("Please enter the amount of time respective to your rate: "))
            return get_annuity_pv(payment, rate, time)
        case 2: 
            payment = float(input("Please enter the payment per period: "))
            rate = float(input("Please enter the rate: "))
            time = int(input("Please enter the amount of time respective to your rate: "))
            return get_annuitydue_pv(payment, rate, time)
        case 3: 
            payment = float(input("Please enter the payment amount per period: "))
            discountRate = float(input("Please enter the discount rate: "))
            growthRate = float(input("Please enter the growth rate (0 if not growing): "))
            return get_perpetuity_pv(payment, discountRate, growthRate)
        case _:
            print("Please enter a valid number!")
            return annuityChoice()

def get_annuity_pv(pmt, r, n):
    pv = (pmt * (1 - (1+r)**(-n)))/r
    return pv

def get_annuitydue_pv(pmt, r, n):
    return get_annuity_pv(pmt, r, n) * (1+r)

def get_perpetuity_pv(pmt, r, g):
    return pmt/(r-g)

def get_npv(initial, cashFlow, rate):
    cash_flows = [float(x) for x in cashFlow.split(",")]
    final = 0

    for i in range(0, len(cash_flows)):
        final += cash_flows[i] / ((1 + rate) ** (i + 1))

    return final - initial

while choice != 5:
    displayMenu()

    choice = int(input())

    match choice:
        case 1:
            horizontalLine()
            principal = float(input("Please input a principal amount: "))
            rate = float(input("Please input the rate as a decimal: "))
            time = int(input("Please input the amount of time respective to your rate: "))
            print(f"\nThe future value of your inputs are ${FV_calculator(principal, rate, time):.2f}.")

        case 2: 
            horizontalLine()
            fv = float(input("Please input a future value amount: "))
            rate = float(input("Please input the discount rate as a decimal: "))
            time = int(input("Please input the amount of time respective to your rate: "))
            print(f"\nThe present value of your inputs are ${PV_calculator(fv, rate, time):.2f}")

        case 3: 
            horizontalLine()
            returnVal = annuityChoice()
            print(f"The annuity present value is ${returnVal:.2f}.")

        case 4: 
            horizontalLine()
            initial = float(input("Please enter the initial investment: "))
            cashflow = input("""Please enter the cashflow amount per year separated by commas: 
Sample input: 1000,1039.12,2020.13,3000
""")
            rate = float(input("Please enter the rate: "))
            print(f"The resulting NPV is ${get_npv(initial, cashflow, rate):.2f}.")

        case _:
            horizontalLine()
            print("Please select a valid choice!")
            
