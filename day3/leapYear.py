year = int(input("Enter the year: "))

if year % 4 == 0 & year % 100 == 0:
    print("It's a leap year!")
elif year % 4 == 0 & year % 400 == 0:
    print("It's a leap year!")
else:
    print("Not a leap year.") 
