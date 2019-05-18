import pickle

# imelda = ("More Mayhem", "Imelda May", "2011", ((1, "Pulling the Rug"),
#                                                 (2, "Psycho"),
#                                                 (3, "Mayhem"),
#                                                 (4, "Kentish Town Waltz"))
#           )
#
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)
# #
# with open("imelda.pickle", 'rb') as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
#
# album, artist, year, tracks = imelda2
# print("Album: {}".format(album))
# print("Artist: {}".format(artist))
# print("Year: {}".format(year))
# print("Tracks: ")
# for track in tracks:
#     print("{}. {}".format(track[0], track[1]))
##
# imelda = ("More Mayhem", "Imelda May", "2011", ((1, "Pulling the Rug"),
#                                                 (2, "Psycho"),
#                                                 (3, "Mayhem"),
#                                                 (4, "Kentish Town Waltz"))
#           )
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
#     pickle.dump(even, pickle_file, protocol=0)
#     pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#     pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#
# with open("imelda.pickle", 'rb') as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
#     even_list = pickle.load(imelda_pickle)
#     odd_list = pickle.load(imelda_pickle)
#     x = pickle.load(imelda_pickle)
#
# print(imelda2)
#
# album, artist, year, tracks = imelda2
# print("Album: {}".format(album))
# print("Artist: {}".format(artist))
# print("Year: {}".format(year))
# print("Tracks: ")
# for track in tracks:
#     print("{}. {}".format(track[0], track[1]))
#
# print("=" * 40)
#
# for i in even_list:
#     print(i)
#
# print("=" * 40)
#
# for i in odd_list:
#     print(i)
#
# print("=" * 40)
#
# print(x)
# #
pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")
