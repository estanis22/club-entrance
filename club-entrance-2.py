# Prompt the user to enter their age and convert the input to an integer

age = int(input("Please enter your age: "))

has_permission = True if age >= 18 else False

if has_permission:
    print("Thank you, welcome!")
else:
    print("You cannot proceed.")