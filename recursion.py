#A way of solving a problem by a function calling itself
#It uses stack memory
#No. of time function is called, It gets stored in stack memory
def RecursiveCall(n):
    if n<1:
        print("n is less than 1")
    else:
        RecursiveCall(n-1)
        print(n)
#RecursiveCall(4)
#RecursiveCall(3)
#RecursiveCall(2)
#RecursiveCall(1)
#RecursiveCall(0)
RecursiveCall(5)
