#BMI calculator 2.0

height = float(input("Enter your height in Meter: "))

weight = int(input("Enter your weight in KG: "))

bmi = int(weight/(height*height))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly ovweweight.")
elif bmi <35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese. ")