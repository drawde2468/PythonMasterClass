# for i in range(0, 10):
#     print("i is now {}".format(i))
##
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
##
# availableExits = ["east", "north east", "south"]
#
# chosenExit = ""
#
# while chosenExit not in availableExits:
#     chosenExit = input("Please choose a direction: ")
#     if chosenExit == "quit":
#         print("Game over")
#         break
# else:
#     print("Aren't you glad you got out of there!")
##

import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
print("Type 0 to exit.")
guess = None
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("The correct number was {}. Exiting...".format(answer))
        break
    if guess < answer:
        print("Too low! Guess higher!")
    elif guess > answer:
        print("Too high! Guess lower!")
else:
    print("Your guess of {} is correct!".format(guess))
