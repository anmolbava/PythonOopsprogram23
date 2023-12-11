# python program to print name ten times via function calling

def functoprintname(n):
    print("Printing the function name times", n)
    print("this print statement was added by developer")
    print("HELLO WORLD")


n = int(input())
for i in range(0,n):
    functoprintname(n)