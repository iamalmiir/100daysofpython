def greet(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    print(f"Hello {name}")

n = "Almir"

greet(n)
def greet_with(name, location):
    print(f"Hello {name},")
    print(f"Let's meet at {location}.")

greet_with("Almir", "Bono")
import random

h = int(input("Height of the wall: \n"))
w = int(input("Width of the wall: \n"))
r = round(h * w)
n = 5

def p(height, width):
    print(f"You will need: {r / n} paint cans.")

p(h, w)