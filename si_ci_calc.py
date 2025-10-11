p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time in years: "))
SI=(p*r*t)/100
print("The Simple Interest is:", SI)
CI=p*(1+r/100)**t - p
print("The Compound Interest is:", CI)
# Simple Interest and Compound Interest Calculator