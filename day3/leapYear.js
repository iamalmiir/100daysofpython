const year = 2000;

year % 4 === 0 && year % 100 === 0
  ? console.log("Leap year.")
  : year % 4 === 0 && year % 400 === 0
  ? console.log("Leap year.")
  : console.log("Not a leap year.");

