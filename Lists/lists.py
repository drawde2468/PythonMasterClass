# ipAddress = input("Please enter an IP Address: ")
# print(ipAddress.count("."))
# #
# parrotList = ["not pinin'", "no more", "a stiff", "bereft of life"]
# parrotList.append("A Norwegian Blue")
# #
# for state in parrotList:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# print(numbers)
# # numbers.sort() #Alternate method but does not return a new list, instead it mutates original
# print(sorted(numbers))
# #
# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("They are equal")
#
# print(list("The Lists are equal"))
# #
# #
# even = [2, 4, 6, 8]
# # anotherEven = even
# anotherEven = list(even)
#
# anotherEven.sort(reverse=True)
#
# print(anotherEven is even)
# print(even == anotherEven)
#
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for numberSet in numbers:
    print(numberSet)

    for value in numberSet:
        print(value)

