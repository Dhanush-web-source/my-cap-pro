#program to print the fibanocci series without using the functions
n=int(input("enter the range of the fib"))
a=0
b=1
c=a+b
for i in range(n):
    print(a)
    a=b
    b=c
    c=a+b
