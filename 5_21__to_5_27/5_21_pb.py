#1
principal1 = 500
rate1 = 0.05
years1 = 3

fv1 = principal1 * (rate1+1) ** 3
print(f"Answer to question 1: {fv1:.2f}")

#2
fv2 = 10000
y2= 5
r = 0.06

pv = fv2 / (1+r) ** y2
print(f"Answer to question 2: {pv:.2f}")

#3 
pv = 1000
r = 0.1
t = 20

fv = pv * (1+r) ** t
print(f"Answer to question 3: {fv:.2f}")

#4
fv = 2000
r = 0.07
t = 4

pv = fv / (1+r) ** t
mini = min(1500, pv)
maxi = max(1500, pv)
print(f"Answer to question 4: {maxi:.2f} is worth more than {mini:.2f}")

#5
print(f"Answer to question 5: Approximate annual return is {72/10:.2f}%")

#6
pv = 800
r = 0.04
t = 6

fv = 800 * (1+r) ** t
print(f"Answer to question 6: {fv:.2f}")

#7
fv = 50000
t = 10
r = 0.08

pv = 50000 / (1+r) ** t
print(f"Answer to question 7: {pv:.2f}")

#8
pv = 200

t1 = 15
r1 = 0.12
fv1 = pv * (1+r1) ** t1

t2 = 180
r2 = 0.01
fv2 = pv * (1+r2) ** t2
print(f"Answer to question 8: {fv1:.2f} for years and {fv2:.2f} for months")

#9
pv = 1000
fv = 3000
t = 12
r = ((fv/pv) ** (1/t)) - 1
print(f"Answer to question 9: {r*100:.1f}%")

#10
pv = 0
r = 0.06
for year in range(1,6):
    val = 500 / (1+r) ** year
    pv += val
print(f"Answer to question 10: {pv:.2f}")

#11
r = 0.08

fv1 = 10000
t1 = 5

fv2 = 15000
t2 = 10

pv1 = fv1 / (1+r) ** t1

pv2 = fv2 / (1+r) ** t2

if max(pv1, pv2) == pv2:
    chosenVal = fv2
else:
    chosenVal = fv1

print(f"Answer to question 11: {max(pv1, pv2):.2f} is worth more which was from the original value of {chosenVal:.2f}")

#12
r = 0.03
pv = 100
t = 20
fv = pv / (1+r) ** 20
print(f"Answer to question 12: {fv:.2f}")