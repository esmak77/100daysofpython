print("BMI Calculator")
weight = float(input("What is your weight in kg?\n"))
height = float(input("How tall are you in meters?\n"))
bmi = weight / (height ** 2)
final_bmi = round(bmi, 2)
print("Your BMI is: " + str(final_bmi))
if final_bmi < 18.5:
    print("You are underweight")
elif 18.5 <= final_bmi < 25.0:
    print("You have a normal weight")
else:
    print("You are overweight")
