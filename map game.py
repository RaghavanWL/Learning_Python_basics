a = {"location": {0: "meet you next time !",
                  1: "you are in middle of the road.",
                  2: "you are on top of the hill.",
                  3: "you are inside the building.",
                  4: "you are in middle of the valley.",
                  5: "you are in the forest"},
     "points": {0: {"Q": 0},
                1: {"Q": 0, "N": 5, "S": 4, "E": 3, "W": 2},
                2: {"Q": 0, "N": 5},
                3: {"Q": 0, "w": 1},
                4: {"Q": 0, "W": 2, "N": 1},
                5: {"Q": 0, "W": 2, "S": 1}},
     "words": {"quit": "Q",
               "WEST": "W",
               "NORTH": "N",
               "EAST": "E",
               "SOUTH": "S"}}
myLocation = 1
while True:
    print("-"*50)
    print(a["location"][myLocation])
    if myLocation == 0:
        break
    availableLocation = ", ".join(a["points"][myLocation].keys())
    print("Where do you want to go ?", availableLocation)
    answer = input("=>").upper()
    answer2 = answer.split()
    if len(answer) > 1:
        for i in answer2:
            if i in a["words"]:
                answer = a["words"][i]
    if answer in a["points"][myLocation]:
        myLocation = a["points"][myLocation][answer]
    else:
        print("this direction is not available")
