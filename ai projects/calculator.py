def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1 / num2)


def calculate(num1, operator, num2):

    if operator == "+":
        add(num1, num2)

    elif operator == "-":
        subtract(num1, num2)

    elif operator == "*":
        multiply(num1, num2)

    elif operator == "/":
        divide(num1, num2)

    else:
        print("Invalid operator")


while True:

    num1 = input("First number: ")

    if num1 == "exit":
        break

    num1 = int(num1)

    operator = input("Enter + - * / : ")

    num2 = input("Second number: ")

    if num2 == "exit":
        break

    num2 = int(num2)

    calculate(num1, operator, num2)