# Dictionary
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)


# Factorial using recursion
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

num = 5
print("Factorial of", num, "is", factorial(num))


# Prime number check
num = 11
if num > 1:
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# Fibonacci series
n = 10
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2

print()
