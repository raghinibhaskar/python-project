# Boolean values

a = 300
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


c = 788
d = 67

if c > d:
    print("c is greater than d")
else:
    print("c is not greater than d")


# Operators

x = 5
y = 10
print(x + y)

x = 10
y = 5
print(x - y)

x = 10
y = 15
print(x * y)

x = 10
y = 2
print(x / y)

x = 5
y = 2
print(x % y)

x = 2
y = 5
print(x ** y)

x = 15
y = 2
print(x // y)

x = 25
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#assigment operators
x = 5
print(5)

x = 6
x += 5
print(x)

x = 7
x -= 3
print(x)

# Assignment Operators in One Program

# = Operator
x = 5
print("= :", x)

# += Operator
x += 3
print("+= :", x)

# -= Operator
x -= 3
print("-= :", x)

# *= Operator
x *= 3
print("*= :", x)

# /= Operator
x /= 3
print("/= :", x)

# %= Operator
x %= 3
print("%= :", x)

# //= Operator
x = 10
x //= 3
print("//= :", x)

# **= Operator
x = 2
x **= 3
print("**= :", x)

# &= Operator
x = 5
x &= 3
print("&= :", x)

# |= Operator
x = 5
x |= 3
print("|= :", x)

# ^= Operator
x = 5
x ^= 3
print("^= :", x)

# >>= Operator
x = 8
x >>= 2
print(">>= :", x)

# <<= Operator
x = 5
x <<= 2
print("<<= :", x)

# := Operator (Walrus Operator)
print(":= :", (y := 3))

#comparison operator
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#logical operator 
# AND

x = 5
y = 10

if x < 10 and y > 5:
    print("AND is True")


# OR

a = 2
b = 8

if a > 5 or b > 5:
    print("OR is True")


# NOT

c = False

if not c:
    print("NOT is True")

 #identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#membership in strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# if condition

age = 18

if age >= 18:
    print("Adult")


# if else condition

number = 5

if number > 0:
    print("Positive")
else:
    print("Negative")


# if elif else condition

marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 50:
    print("Pass")

else:
    print("Fail")