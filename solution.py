# It is almost December and Sophia, the latest AI robot coming for Python Boot camp v.2.
#  As a smart robot she wants to evaluate all the possible ways she can get to the location.
#  The dynamic and sophisticated features that Sophia has, enables her to move in four Directions;
#  Left, Right, Up and down.
# Below are the 3 different options she has in making the shortest Journey with minimal energy cost
#  (rated in Ghana Cedis):
# NB: Distance is measured in steps. The Options are represented by a tuple.
# Option 1 (Cost, Direction, Steps taken):
# •	(10, LEFT, 30)
# •	(7, RIGHT, 45)
# •	(15, UP, 15)
# •	(20, DOWN, 20)
# Option 2 (Cost, Direction, Steps taken):
# •	(12, LEFT, 49)
# •	(5, RIGHT, 42)
# •	(18, UP, 12)
# •	(15, DOWN, 14)
# a.	Write a python program that would compute the distance after a sequence
#    of movements by Sophia in any direction. Take the starting point as (0, 0).
# b.	 If the distance is a float, then round it off to 2 decimal places and print it to the Screen.
# c.	Which of the Options give the shortest distance to the location?
# d.	Which of the Options expends the least amount of energy?

                            #####  QUESTION ABOOVE, ANSWER BELOW #########

import math

# OPTIONS
option_1 = [(10, "LEFT", 30), (7, "RIGHT", 45), (15, "UP", 15), (20, "DOWN", 20)]
option_2 = [(12, "LEFT", 49), (5, "RIGHT", 42), (18, "UP", 12), (15, "DOWN", 14)]

origin = (0, 0)


# Creating a function to take array as input
def sophia(arr):
    cost = 0
    # x_Direction
    direction_x = origin[0]

    # y_Direction
    direction_y = origin[1]

    # looping through arrays
    for i in range(len(arr)):
        if arr[i][1] == "LEFT":
            direction_x = direction_x - arr[i][2]
            cost = cost + arr[i][0]

        elif arr[i][1] == "RIGHT":
            direction_x = direction_x + arr[i][2]
            cost = cost + arr[i][0]

        elif arr[i][1] == "DOWN":
            direction_y = direction_y - arr[i][2]
            cost = cost + arr[i][0]

        else:
            direction_y = direction_y + arr[i][2]
            cost = cost + arr[i][0]

    distance = round(math.sqrt((direction_x) ** 2 + (direction_y) ** 2), 2)
    return distance, cost


(distance_1, cost_1) = sophia(option_1)
(distance_2, cost_2) = sophia(option_2)

print("OPTION 1(distance, cost) = " + str((distance_1, cost_1)))
print("OPTION 2(distance, cost) = " + str((distance_2, cost_2)))

if distance_1 < distance_2:
    print("OPTION_1 gives the shortest possible distance")
else:
    print("OPTION_2 gives the shortest possible distance")

if cost_1 < cost_2:
    print("OPTION_1 expends the least amount of energy")
else:
    print("OPTION_2 expends the least amount of energy")





