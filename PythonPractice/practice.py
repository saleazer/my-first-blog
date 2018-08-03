name = input("What's your name?")
print("Hello,", name)
age = int(input("Can you tell me your age?"))
print("Wow %s You're %s years old!" % (name, age))
year = str((2018 - age)+ 100)
answer = input("Do you want to know what year you will turn 100?")
if answer == "yes":
    print("You will turn 100 in the year" + year)
else:
    print("Too bad, I'm telling you anyway. It will be in the year " + year + ".")