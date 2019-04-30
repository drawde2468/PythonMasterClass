name = input("What is your name? ")
age = int(input("How old are you, {0}? ".format(name)))

if 18 <= age <= 30:
    print("Welcome to the holiday, {}!".format(name))
else:
    print("I'm sorry {}, you must be aged 18 to 30 to attend this party.".format(name))
