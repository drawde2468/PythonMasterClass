typedString = input("Enter some text")

# vowelSet = {'a', 'e', 'i', 'o', 'u', 'y', ' '}
vowelSet = frozenset("aeiou ")

finalSet = set(typedString).difference(vowelSet)
print(finalSet)

finalList = sorted(finalSet)

print(finalList)
