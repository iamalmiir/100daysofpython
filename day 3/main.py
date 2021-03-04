age = int(input("What's your age? "));
if age >= 18:
    print("you can ride fucker!")
else: 
    print("Oh shit!")

number = int(input("Type in the number: "))
if number % 2 == 0:
    print("It's even number!")
else:
    print("Not even number!")
height = int(input("What is your height in CM? "))
age = int(input("How old are you? "))

if height >= 120:
    if age >= 18:
        print("You can ride. Price for the ticket will be $20")
    elif age < 12:
        print("You can ride. Price for the ticket will be $7")
    elif age < 18:
        print("You can ride. Price for the ticket will be $12")
    else:
        print("You can't ride.")
else:
    print("You can't ride.")

if height >= 120:
    if age >= 18:
        print("You can ride. Price for the ticket will be $20")
    else:
        print("You can ride. Price for the ticket will be $15")
else:
    print("You need to grow up taller than 120cm. Sorry.")

weight = float(input("What is your weight in kg? "))
height = float(input("What is your height? "))

breakItdown = round(weight / height ** 2);

if breakItdown <= 18.5:
    print(f"You are under weight. Your bmi is: {breakItdown}")
elif breakItdown <= 25:
    print(f"You are normal weight. Your bmi is: {breakItdown}")
elif breakItdown <= 30:
    print(f"You are slightly overweight. Your bmi is: {breakItdown}")
elif breakItdown <= 35:
    print(f"You are obese. Your bmi is: {breakItdown}")
else:
    print(f"You are clinically obese! Your bmi is: {breakItdown}")
