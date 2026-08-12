def factorial(n):
    if n<=1:
        return 1
    return n*(factorial(n-1))
print(factorial(4))
#4*factorial(3)
#3*factorial(2)
#1*factorial(1)
#4*3*2*1=24