fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
#
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# fruit["lime"] = "great with tequila"
# print(fruit)
#
# # del fruit["lemon"]
# # print(fruit)
# # fruit.clear()
# # print(fruit)
#
# # print(fruit["tomato"])

# print(fruit)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a {}".format(dict_key))
#     print(description)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("We don't have a " + dict_key)
##
# for snack in fruit:
#     print(fruit[snack])
##
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("=" * 40)
##
# orderedKeys = list(fruit.keys())
# orderedKeys.sort()
# orderedKeys = sorted(list(fruit.keys()))
# for key in orderedKeys:
#     print("{0}: {1}".format(key, fruit[key]))
##
# for key in sorted(fruit.keys()):
#     print("{0}: {1}".format(key, fruit[key]))
# # better to use keys, it's more efficient
# for val in fruit.values():
#     print(val)
# print("=" * 40)
# for key in fruit:
#     print(fruit[key])
# #

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
# #
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)
for snack in f_tuple:
    item, description = snack
    print("{a} is {b}".format(a=item, b=description))

print(dict(f_tuple))

