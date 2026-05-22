def get_annuity_pv(pmt, r, n):
    pv = (pmt * (1 - (1+r)**(-n)))/r
    return pv

def get_annuitydue_pv(pmt, r, n):
    return get_annuity_pv(pmt, r, n) * (1+r)

def get_perpetuity_pv(pmt, r, g=0):
    return pmt/(r-g)

#1
pv = get_annuity_pv(300, 0.06, 5)
print(f"Answer to question 1: ${pv:.2f}")

#2
pv = get_annuitydue_pv(300, 0.06, 5)
print(f"Answer to question 2: ${pv:.2f}")

#3
pv = get_perpetuity_pv(1000, 0.05)
print(f"Answer to question 3: ${pv:.2f}")

#4
pv = get_perpetuity_pv(1000, 0.08)
print(f"Answer to question 4: the value decreases (${pv:.2f}), this matters because it shows how a higher discount rate lowers the value for perpetuities.")

#5 
initial = 4000
final = get_annuity_pv(1200, 0.07, 4)
npv = final - initial

print(f"Answer to question 5: the NPV is ${npv:.2f}, since this value is greater than 0, it is a worthwhile investment.")

#6 
bond = get_annuity_pv(50, 0.04, 6)
final = 1000/((1.04)**6)
pv = bond + final

print(f"Answer to question 6: the total value of the bond is ${pv:.2f}.")

#7
pmt = (20000 * 0.05) / (((1+0.05)**6)-1)
print(f"Answer to question 7: ${pmt:.2f}")

#8
pv = get_perpetuity_pv(500, 0.75/100)
print(f"Answer to question 8: ${pv:.2f}")

#9
optionA = 5000
optionB = get_annuity_pv(800, 0.06, 8)

print(f"Answer to question 9: the better option is ${max(optionA, optionB):.2f}.")

#10
optionB = get_annuity_pv(800, 0.1, 8)

print(f"Answer to question 10: the better option is ${max(optionA, optionB):.2f}. It does not change because increasing the discount rate just decreases the present value.")

#11
initial = 10000
final = get_annuity_pv(2500, 0.06, 5)
npv = final - initial

print(f"Answer to question 11: the NPV is ${npv:.2f}. If this value is greater than 0 the investment is good.")

#12
pv = get_perpetuity_pv(100, 0.07, 0.02)
print(f"Answer to question 12: ${pv:.2f}")