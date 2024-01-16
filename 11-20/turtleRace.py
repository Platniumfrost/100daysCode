from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Zip the two lists together
combined = list(zip(y_positions, colors))

# Sort based on y_positions
sorted_combined = sorted(combined)

# Unpack the sorted pairs
sorted_y_positions, sorted_colors = zip(*sorted_combined)

# Display the sorted lists
print("Original Colors:", colors)
print("Original Y Positions:", y_positions)
print("\nSorted Colors:", sorted_colors)
print("Sorted Y Positions:", sorted_y_positions)

# All Turtles are created here
turtles = []
for turtle_index in range(0, 6):
    one_turtle = Turtle(shape="turtle")
    one_turtle.penup()
    one_turtle.color(colors[turtle_index])
    one_turtle.goto(x=-230, y=sorted_y_positions[turtle_index])
    turtles.append(one_turtle)

# Betting mechanism (input from user)
bet = input("Enter your bet color: ")  # User inputs the desired color
race_commencing = True

while race_commencing:
    for turtle in turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            race_commencing = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            # You may choose to exit the loop or take additional actions after the race ends.

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen = Screen()
screen.exitonclick()
