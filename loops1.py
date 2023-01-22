## pattern 1
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

## pattern 2
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()

## pattern 3
n = int(input("Enter the number of rows: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == (n - 1) or row == col:
            print("*", end="")
        else:
            print(end=" ")
    print()

## factorial number inbuilt function
import math
n = int(input("Enter the number: "))
result = math.factorial(n)
print("factorial of", n, "is", result)

## factorial number recursion


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


n = int(input("Enter the number: "))
result = fact(n)
print("factorial of", n, "is", result)

## factorial number loops
n = int(input("Enter the number: "))
result = 1
for i in range(n, 0, -1):
    result = result * i

print("factorial of", n, "is", result)

## pattern program
n = int(input("Enter the number of rows: "))
for row in range(0, n):
    for col in range(0, n):
        if row == 0 or col == n - 1 or row == col:
            print("*", end="")
        else:
            print(end=" ")
    print()

## pattern program

n = int(input("Enter the number of row: "))
num = 1
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(num, end="")
        num = num + 1
    print()

## pattern program
string = input("Enter the string: ")
length = len(string)
for row in range(length):
    for col in range(row + 1):
        print(string[col], end="")
    print()

## fibonacci series :
n = int(input("Enter how many numbers you want in this series:"))
first = 0
second = 1
for i in range(n):
    print(first)
    temp = first
    first = second
    second = temp + second

## patern program:
n = int(input("Enter the number of rows: "))
for row in range(n, 0, -1):
    for col in range(1, row + 1):
        print(row, end="")
    print()

## prime numbers

lower = int(input("Enter the lower interval: "))
upper = int(input("Enter the upper interval: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

## prime number check
num = int(
    input("Enter any positive number to check whether it is prime or not: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, " is a prime number")
else:
    print("number is negative or less than or equal to 1")

## pattern program

n = int(input("Enter the number of rows: "))
for row in range(1, n + 1):
    for col in range(1, 2 * n):
        if row == n or row + col == n + 1 or col - row == n - 1:
            print("*", end="")
        else:
            print(end=" ")
    print()

## perfect numbers:

num = int(input("Enter the number: "))
result = 0
for i in range(1, num):
    if (num % i) == 0:
        result = result + i
if result == num:
    print(num, "is perfect number")
else:
    print(num, " is not perfect number")

## swapping numbers:
a = 10
b = 5
print(a, b)
temp = a
a = b
b = temp
print(a, b)

## pattern print program
num = int(input("Enter the number of rows: "))
row = 0
while row < num:
    star = row + 1
    while star > 0:
        print("*", end="")
        star = star - 1
    row = row + 1
    print()


## reverse string
def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    print("reversed string is:", reversed_string)


string = input("Enter a string:")
print("Entered string", string)
reverse(string)

## pattern program
num = int(input("Enter the number of rows: "))
n_list = [[0 for x in range(num)] for y in range(num)]
n = 1
low = 0
high = num - 1
count = int((num + 1) / 2)

for i in range(count):
    for j in range(low, high + 1):
        n_list[i][j] = n
        n = n + 1
    for j in range(low + 1, high + 1):
        n_list[j][high] = n
        n = n + 1
    for j in range(high - 1, low - 1, -1):
        n_list[high][j] = n
        n = n + 1
    for j in range(high - 1, low, -1):
        n_list[j][low] = n
        n = n + 1
    low = low + 1
    high = high - 1

for i in range(num):
    for j in range(num):
        print(n_list[i][j], end="\t")
    print()

## GCD OF TWO NUMBERS:


def computeGCD(a, b):
    if b == 0:
        return a
    else:
        return computeGCD(b, a % b)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(computeGCD(num1, num2))

## pattern program

num = int(input("Enter the number of rows: "))
for i in range(1, num + 1):
    for j in range(1, num - i + 1):
        print(end=" ")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()

## pattern program
