p=100000
r=12
n=3
t=5
A=p*(1+r*t)
B=p*(1+r/n)**(n*t)
print(f"the simple intrest with intrest rate {r} is {A}")
print(f"the compound intrest with same intrest is {B}")