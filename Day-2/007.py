# BMI (Body Mass Index) Calculator 

# 1st input: enter height in meters e.g: 1.65
height = input()

# 2nd input: enter weight in kilograms e.g: 72
weight = input()


weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2;

print("Your BMI is: ",bmi ); 
