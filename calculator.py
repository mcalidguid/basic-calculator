# A simple calculator that accepts two numbers and performs basic arithmetic operations.


def read_input():
    x = float(input("1st number: "))
    y = float(input("2nd number: "))
    return x, y


def print_result(x):
    try:
        print(">>>: The answer is %.2f" % x)
    except TypeError:
        print(">>>: Try Again.")


def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        print(">>>: Error: You are trying to divide a number by zero.")


while True:
    print("""---------------------
    Select an option:
        Enter \"+\" for addition
        Enter \"-\" for subtraction
        Enter \"*\" for multiplication
        Enter \"/\" for division
        Enter \"q\" to quit""")
    user_input = input(">>>: ")

    if user_input == "q":
        print(">>>: Danke, tschüss!~")
        break

    elif user_input == "+":
        first_number, second_number = read_input()
        result = add(first_number, second_number)
        print_result(result)

    elif user_input == "-":
        first_number, second_number = read_input()
        result = subtract(first_number, second_number)
        print_result(result)

    elif user_input == "*":
        first_number, second_number = read_input()
        result = multiply(first_number, second_number)
        print_result(result)

    elif user_input == "/":
        first_number, second_number = read_input()
        result = divide(first_number, second_number)
        print_result(result)

    else:
        print(">>>: Invalid input")
