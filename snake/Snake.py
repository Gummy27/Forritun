import turtle
import time
import random

# Score
high_score = 0
score = 0

delay = 0.1

# Screen
wn = turtle.Screen()
wn.title("Snake Game by Gummy27")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates.

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def collision():
    flag = False
    x = head.xcor()
    y = head.ycor()

    # Border collision
    if(x >= 290 or x <= -290):
        flag = True
    elif(y >= 290 or y <= -290):
        flag = True

    # Body collision
    for i in range(len(segments)):
        if(head.distance(segments[i]) < 20):
            flag = True
    return(flag)



# Keyboard bindings
wn.listen()
# WASD
wn.onkeypress(go_up, "1")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Arrows
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    while True:
        wn.update()

        # Collision
        if head.distance(food) < 20:
            score += 10
            print(score)
            if(score > high_score):
                high_score = score
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Write Score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

        if(collision() == True):
            break

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()

        time.sleep(delay)

    # Hiding the segments
    for segment in segments:
        segment.goto(1000, 1000)
    # Clearing the segment list
    segments.clear()
    segments = []

    # Resetting Values
    head.direction = "stop"
    score = 0
    food.goto(0, 100)
    head.goto(0, 0)
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

wn.mainloop()
