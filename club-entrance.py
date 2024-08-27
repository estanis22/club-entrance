# Prompt the user to enter their age and convert the input to an integer

age = int(input("Please enter your age: "))

if age < 18:
    print("You cannot proceed, you are under 18.")
elif age >= 18 and age <= 65:
    print("Thank you, welcome!")
else:
    print("You are over 65, you cannot proceed.")