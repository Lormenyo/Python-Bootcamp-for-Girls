# Python-Bootcamp-for-Girls

This was a code challenge for the girls to answer in order to win a ticket to the Python conference 2018.
They came up with beautiful solutions.

It mainly involves functions, conditional statements and mathematical reasoning.

# The Question
It is almost December and Sophia, the latest AI robot coming for Python Boot camp v.2.

As a smart robot she wants to evaluate all the possible ways she can get to the location.

The dynamic and sophisticated features that Sophia has, enables her to move in four Directions;
Left, Right, Up and down.Below are the 2 different options she has in making the shortest Journey with minimal energy cost (rated in Ghana Cedis):
NB: Distance is measured in steps. 
The Options are represented by a tuple.

Option 1 (Cost, Direction, Steps taken):
 •	(10, LEFT, 30)
 •	(7, RIGHT, 45)
 •	(15, UP, 15)
 •	(20, DOWN, 20)
 
 Option 2 (Cost, Direction, Steps taken):
 •	(12, LEFT, 49)
 •	(5, RIGHT, 42)
 •	(18, UP, 12)
 •	(15, DOWN, 14)
 
a.	Write a python program that would compute the distance after a sequence
    of movements by Sophia in any direction. Take the starting point as (0, 0).
    
 b.	 If the distance is a float, then round it off to 2 decimal places and print it to the Screen.
 
 c.	Which of the Options give the shortest distance to the location?
 
 d.	Which of the Options expends the least amount of energy?

# HOW THE CODE WORKS
Math module in python was imported to help with the mathematical functions to be used.
The options were defined in the form of an array like so:

```
option_1 = [(10, "LEFT", 30), (7, "RIGHT", 45), (15, "UP", 15), (20, "DOWN", 20)]
```

The origin was defined as a tuple with 0 as the initial x and y position.
`origin = (0, 0)`

A for loop was used to loop through the array. The maths of the program was done using the logic that a left and downwards direction indicates a subtraction whilst a right and upwards direction implies an addition.



