import re
print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("Whats is their name? ")
c = len(re.findall('[true]', name1 + name2))
c1 = len(re.findall('[love]', name1 + name2))
total = c * 10 + c1

if total <= 10 or total >= 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")