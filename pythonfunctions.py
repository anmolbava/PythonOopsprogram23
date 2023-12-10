# python program to print name ten times via function calling

def functoprintname(n):
    print("Printing the function name times", n)

n = int(input())
for i in range(0,n):
    functoprintname(n)