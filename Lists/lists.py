# ipAddress = input("Please enter an IP Address: ")
# print(ipAddress.count("."))
# #
parrotList = ["not pinin'", "no more", "a stiff", "bereft of life"]
parrotList.append("A Norwegian Blue")

for state in parrotList:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)
# numbers.sort() #Alternate method but does not return a new list, instead it mutates original
print(sorted(numbers))

