from art import logo
print(logo)
# Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide   
def divide(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculate():
    s = True
    num1 = float(input("What's the first number?: "))
    while s:
        for symbol in operations:
            print(symbol)
        o_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        total = operations[o_symbol](num1, num2)
        print(f"{num1} {o_symbol} {num2} = {total} ")
        if input(f"Type 'y' to continue calculatin with {total} or type 'n' for new begin, 'e' to end: ") == 'y':
            num1 = total
        else:
            s = False
            calculate()

calculate()