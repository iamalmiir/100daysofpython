import random

random_num = random.randint(1, 100)
print(bla.number)

print(random_num)

number = random.randint(0, 1)

if number == 1:
    print("Head")
else: 
    print("Tails")

names = input("Give me the names? ")
op = names.split(", ")
rn = random.randint(0, len(op)) - 1
print(op[rn])