import numpy as np
from numpy import pi

# Exercise 1
a = np.arange(1,21)
print(f"Answer to question 1:\n {a}")

# Exercise 2
a = np.zeros((4,4))
for i in range(0,4):
    a[i,i] = 1
print(f"Answer to question 2:\n {a}")

# Exercise 3
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(f"""
Answer to question 3:
Addition {a+b}
Subtraction {a-b}
Multiplication Element-Wise {a*b}
Division {np.round(a/b, 2)} 
""")

# Exercise 4
a = np.linspace(0, 2*pi, 100)
sins = np.sin(a)
print(f"""
Answer to question 4:      
First 5: {sins[0:5]}     
Last 5: {sins[-5:]}
""")


# Exercise 5
a = np.arange(1,10)
a.resize((3,3))
print(f"""
Answer to question 5:
First row: {a[0]}     
Second column: {a[:,1]}  
Value at row 2 column 3: {a[1,2]}
""")

# Exercise 6
rng = np.random.default_rng(67)
a = rng.random(1000)

print(f"""
Answer to question 6: 
Mean: {np.round(np.mean(a),2)}      
Median: {np.median(a)}
Min = {np.min(a)}
Max = {np.max(a)}
Standard Deviation = {np.std(a, ddof=1)}
""")

# Exercise 7
a = np.array([3,1,4,1,5,9,2,6])
print(f"""
Answer to question 7:
Sorted array:
{np.sort(a)}
Index of original max:
{np.argmax(a)}
""")

# Exercise 8
a = rng.integers(0, 15, 6)
a.resize((2,3))

b = rng.integers(0, 15, 6)
b.resize((3,2))

print(f"""
Answer to question 8:
Original values of A
{a}
Original values of B
{b}
Resulting Matrix Dot Product
{np.dot(a, b)}    
""")
