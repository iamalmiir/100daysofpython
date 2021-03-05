import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
u = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
c = random.randint(0, 2)
if u >= 3 or u < 0:
    print("Wrong input. Please choose between 0 and 2.")
elif u == 0 and c == 2:
    print(f"{options[u]} \n Computer choose: \n {options[c]} \n You won!")
elif u == 2 and c == 0:
    print(f"{options[u]} \n Computer choose: \n {options[c]} \n Computer won!")
elif u > c:
    print(f"{options[u]} \n Computer choose: \n {options[c]} \n You won!")
elif u < c:
    print(f"{options[u]} \n Computer choose: \n {options[c]} \n Computer won!")
elif u == c:
    print(f"{options[u]} \n Computer choose: \n {options[c]} \n Draw!")
