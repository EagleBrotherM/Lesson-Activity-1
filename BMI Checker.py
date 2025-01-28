height = float(input("Enter Your height in cm: "))
weight = float (input("Enter your weight in kg "))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are Skinny but strong 💪 ")

elif BMI <= 24.9:
    print("You are Healthy💪 ")

elif BMI <= 29.9:
    print("Bro what have you been eating (Overweight) ")

elif BMI <= 34.9:
    print("You are OVER your level 👎 ")

elif BMI <= 39.9:
    print("You are Seriously Fat ")

else:
    print("You Seriously Have to Work Out 🤢")