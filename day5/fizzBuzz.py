for g in range(1, 101):
    if g % 3 == 0 and g % 5 == 0:
        print("FizzBuzz")
    elif g % 3 == 0:
        print("Fizz")
    elif g % 5 == 0:
        print("Buzz")
    else:
        print(g)