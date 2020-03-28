#Exists to follow along and to show how to not screw it up
# Python 2
def factorial(n):
    print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(5)