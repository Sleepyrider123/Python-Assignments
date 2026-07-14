a = float(input("Enter first number: "))
b = float(input('Enter second number: '))

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

add = addition(a,b)
sub = subtraction(a,b)
mul = multiplication(a,b)
div = division(a,b)


user = input('What would you like to do? (add, sub, mul, div): ').upper()

if user == 'ADD':
    print(add)
elif user == 'SUB':
    print(sub)
elif user == 'MUL':
    print(mul)
elif user == 'DIV':
    print(div)
else:
    print("Invalid input")
