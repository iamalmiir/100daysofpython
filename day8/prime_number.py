n = int(input("Pick a number: \n"))

def p(number):
    is_p = True
    for i in range(2, number):
       if number % i == 0:
        is_p = False
    if is_p:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

p(n)
