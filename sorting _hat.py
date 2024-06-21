def sorting_hat():
    houses = {
        "Gryffindor": 0,
        "Ravenclaw": 0,
        "Hufflepuff": 0,
        "Slytherin": 0
    }

    # Question 1
    print("Q1) Do you like Dawn or Dusk?")
    print("1) Dawn")
    print("2) Dusk")
    answer1 = int(input("Your answer: "))
    
    if answer1 == 1:
        houses["Gryffindor"] += 1
        houses["Ravenclaw"] += 1
    elif answer1 == 2:
        houses["Hufflepuff"] += 1
        houses["Slytherin"] += 1
    else:
        print("Wrong input.")
        return

    # Question 2
    print("Q2) When I’m dead, I want people to remember me as:")
    print("1) The Good")
    print("2) The Great")
    print("3) The Wise")
    print("4) The Bold")
    answer2 = int(input("Your answer: "))
    
    if answer2 == 1:
        houses["Hufflepuff"] += 2
    elif answer2 == 2:
        houses["Slytherin"] += 2
    elif answer2 == 3:
        houses["Ravenclaw"] += 2
    elif answer2 == 4:
        houses["Gryffindor"] += 2
    else:
        print("Wrong input.")
        return

    # Question 3
    print("Q3) Which kind of instrument most pleases your ear?")
    print("1) The violin")
    print("2) The trumpet")
    print("3) The piano")
    print("4) The drum")
    answer3 = int(input("Your answer: "))
    
    if answer3 == 1:
        houses["Slytherin"] += 4
    elif answer3 == 2:
        houses["Hufflepuff"] += 4
    elif answer3 == 3:
        houses["Ravenclaw"] += 4
    elif answer3 == 4:
        houses["Gryffindor"] += 4
    else:
        print("Wrong input.")
        return

    # Determine the house with the most points
    max_points = max(houses.values())
    winning_houses = [house for house, points in houses.items() if points == max_points]

    if len(winning_houses) == 1:
        print(f"The Sorting Hat has decided: {winning_houses[0]}!")
    else:
        print(f"The Sorting Hat has decided on a tie between: {' and '.join(winning_houses)}!")

# Run the sorting hat program
sorting_hat()