def greet():
    print("Hello World")

greet()

# functions with parameters 
def greet(name):
    print("Hello", name)

greet("Raghini")

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Raghini")

def hello():
    print("Hello")

def world():
    hello()
    print("World")

world()

def count():
    for i in range(5):
        print(i)

count()

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

for i in range(1, 6):
    print(i, check_even(i)) 