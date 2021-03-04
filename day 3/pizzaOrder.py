size =  input("What size: S, M or L? ")
add_pepperoni = input("Do you want extra pepperoni? ")
add_cheese = input("Do you want extra cheese? ")
age = int(input("How old are you? "))
bill = 0;

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if add_cheese == "Y":
    bill += 1
print(bill)
