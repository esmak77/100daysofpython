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
elif 25.0 <= final_bmi < 30.0:
    print("You are overweight")
elif 30.0 <= final_bmi:
    print("You are obese")
else:
    print("You put the wrong input.")