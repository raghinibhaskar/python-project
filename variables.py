x = 21
y = "raghini"
print(x)
print(y)

z = 21
z = "raghini" 
print(z)

a = 6
b = "rina"
print(type(a))
print(type(b))

x , y , z = "apple", "cherry","orange"
print(x)
print(y)
print(z)

x = y = z = "raghini"
print(x)
print(y)
print(z)

toys = ["car","bike","bus"]
x , y , z = toys
print(x)
print(y)
print(z)

x = "I work as a intern at nerdshub"
print(x)

a = "heyy"
b = "there"
print(a , b)

f = "wassup"
h = "how you doing"
k = "today?"
print(f + h + k)

x = 12
y = 56
print(x + y)

x = "beautiful"

def myfunc():
    print("Chennai is " + x)

myfunc()

def myfunc():
  global x
  x = "beautiful"

myfunc()

print("chennai is " + x)

# concepts covered from variables :

# Integer variable
age = 21
print(age)

# String variable
name = "raghini"
print(name)

# Changing variable type
z = 21
z = "raghini"
print(z)

# Checking data types
a = 6
b = "rina"

print(type(a))
print(type(b))

# Multiple variable assignment
x, y, z = "apple", "cherry", "orange"

print(x)
print(y)
print(z)

# Same value to multiple variables
p = q = r = "beautiful"

print(p)
print(q)
print(r)

# Unpacking a list
toys = ["car", "bike", "bus"]

toy1, toy2, toy3 = toys

print(toy1)
print(toy2)
print(toy3)

# Printing text
x = "I work as an intern at nerdshub"
print(x)

# Printing multiple variables
a = "heyy"
b = "there"

print(a, b)

# String concatenation
f = "wassup "
h = "how you doing "
k = "today?"

print(f + h + k)

# Adding numbers
num1 = 12
num2 = 56

print(num1 + num2)

# Global variable
city = "beautiful"

def myfunc():
    print("Chennai is " + city)

myfunc()

# Creating global variable inside function
def myfunc2():
    global x
    x = "awesome"

myfunc2()

print("Python is " + x)