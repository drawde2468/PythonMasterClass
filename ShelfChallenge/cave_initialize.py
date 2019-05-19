import shelve

# MY SOLUTION
# with shelve.open('gameData') as game_initialize:
#     game_initialize["locations"] = {"0": {"desc": "You are sitting in front of a computer learning Python",
#                                           "exits": {},
#                                           "namedExits": {}},
#                                     "1": {"desc": "You are standing at the end of a road before a small brick building",
#                                           "exits": {"W": "2", "E": "3", "N": "5", "S": "4", "Q": "0"},
#                                           "namedExits": {"2": "2", "3": "3", "5": "5", "4": "4"}},
#                                     "2": {"desc": "You are at the top of a hill",
#                                           "exits": {"N": "5", "Q": "0"},
#                                           "namedExits": {"5": "5"}},
#                                     "3": {"desc": "You are inside a building, a well house for a small stream",
#                                           "exits": {"W": "1", "Q": "0"},
#                                           "namedExits": {"1": "1"}},
#                                     "4": {"desc": "You are in a valley beside a stream",
#                                           "exits": {"N": "1", "W": "2", "Q": "0"},
#                                           "namedExits": {"1": "1", "2": "2"}},
#                                     "5": {"desc": "You are in the forest",
#                                           "exits": {"W": "2", "S": "1", "Q": "0"},
#                                           "namedExits": {"2": "2", "1": "1"}}
#                                     }
#     game_initialize["vocabulary"] = {"QUIT": "Q",
#                                      "NORTH": "N",
#                                      "SOUTH": "S",
#                                      "EAST": "E",
#                                      "WEST": "W",
#                                      "ROAD": "1",
#                                      "HILL": "2",
#                                      "BUILDING": "3",
#                                      "VALLEY": "4",
#                                      "FOREST": "5"}
#
#     # for testing
#     location_keys = sorted(list(game_initialize["locations"].keys()))
#
#     for key in location_keys:
#         print(game_initialize["locations"][key]["desc"])
#     print(game_initialize["vocabulary"])
# #

#SECOND SOLUTION

with shelve.open('locations') as locations:
    # locations["0"] = {"desc": "You are sitting in front of a computer learning Python",
    #                   "exits": {},
    #                   "namedExits": {}}
    # locations["1"] = {"desc": "You are standing at the end of a road before a small brick building",
    #                   "exits": {"W": "2", "E": "3", "N": "5", "S": "4", "Q": "0"},
    #                   "namedExits": {"2": "2", "3": "3", "5": "5", "4": "4"}}
    # locations["2"] = {"desc": "You are at the top of a hill",
    #                   "exits": {"N": "5", "Q": "0"},
    #                   "namedExits": {"5": "5"}}
    # locations["3"] = {"desc": "You are inside a building, a well house for a small stream",
    #                   "exits": {"W": "1", "Q": "0"},
    #                   "namedExits": {"1": "1"}}
    # locations["4"] = {"desc": "You are in a valley beside a stream",
    #                   "exits": {"N": "1", "W": "2", "Q": "0"},
    #                   "namedExits": {"1": "1", "2": "2"}}
    # locations["5"] = {"desc": "You are in the forest",
    #                   "exits": {"W": "2", "S": "1", "Q": "0"},
    #                   "namedExits": {"2": "2", "1": "1"}}

    print(sorted(list(locations.keys())))

with shelve.open('vocabulary') as vocabulary:
    # vocabulary["QUIT"] = "Q"
    # vocabulary["NORTH"] = "N"
    # vocabulary["SOUTH"] = "S"
    # vocabulary["EAST"] = "E"
    # vocabulary["WEST"] = "W"
    # vocabulary["ROAD"] = "1"
    # vocabulary["HILL"] = "2"
    # vocabulary["BUILDING"] = "3"
    # vocabulary["VALLEY"] = "4"
    # vocabulary["FOREST"] = "5"

    print(list(vocabulary.keys()))
