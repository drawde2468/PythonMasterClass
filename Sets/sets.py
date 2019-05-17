# farmAnimals = {"sheep", "cow", "hen"}
# print(farmAnimals)
#
# for animal in farmAnimals:
#     print(animal)
#
# print("=" * 40)
#
# wildAnimals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wildAnimals)
#
# for animal in wildAnimals:
#     print(animal)
#
# farmAnimals.add("horse")
# wildAnimals.add("horse")
#
# print(farmAnimals)
# print(wildAnimals)
# #
# emptySet = set()
# emptySet2 = {}
# emptySet.add("a")
# # emptySet2.add("a")  # cannot create set in this manner, creates dictionary instead
# #
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# #
# even = set(range(0,40,2))
# print(even)
# print(len(even))
# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("="*40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
# #
# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)
#
# print("=" * 40)
#
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))
# #
# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))
# #
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
#
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # no error, does nothing
# print(squares)
# try:
#     squares.remove(8)
# except KeyError:
#     print("Item 8 is not a member of the set")
# #
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16,)
# squares = set(squares_tuple)
# print(squares)
#
# if squares.issubset(even):
#     print("square is a subset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")
#
even = frozenset(range(0,100,2))
print(even)


