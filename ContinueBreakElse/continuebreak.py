# shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice", ]
# for item in shoppingList:
#     if item == "spam":
#         continue
#
#     print("Buy " + item)

meal = ["egg", "bacon", "beans", "sausages"]
nastyFoodItem = ''

for item in meal:
    if item == 'spam':
        nastyFoodItem = item
        break
else:
    print("I'll have a plate of that then please.")

if nastyFoodItem:
    print("Can't I have anything without spam in it!")
