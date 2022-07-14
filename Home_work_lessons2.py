name = input("What is your name ? \t")
age = input(f"{name} how old are you?  \t")
if 16 < int(age) < 70 or 90 < int(age) <= 121:
    print(f"Welcome {name} on our website.")
elif int(age) == 16:
    print(f"Dear {name} need to wait one year.")
elif 70 <= int(age) <= 90:
    print(f"You are lucky {name} and welcome.")
elif int(age) > 121:
    print(f"You are not real {name}.")
else:
    print(f"I'm sorry {name} you are too young.")
