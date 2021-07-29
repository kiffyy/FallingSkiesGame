import turtle
import random


score = 0

wn = turtle.Screen()
wn.title("Falling skies by Kiffy")
wn.bgcolor("lightblue")

wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("donut.gif")
wn.register_shape("monster.gif")
wn.register_shape("cupcake.gif")
wn.register_shape("icecream.gif")
wn.register_shape("poison.gif")

# adding the player
player = turtle.Turtle()
player.speed(0)
player.shape("monster.gif")
player.color("red")
player.penup()
player.goto(0, -250)

player.direction = "stop"

# CREATE A LIST OF GOOD GUYS
good_guys = []

# adding the good guy
for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("cupcake.gif")
    good_guy.color("yellow")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guy.speed = random.randint(1, 2)
    good_guys.append(good_guy)

# CREATE A LIST OF BAD GUYS
bad_guys = []

# adding thebad
for _ in range(5):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("poison.gif")
    bad_guy.color("purple")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guy.speed = random.randint(1, 2)
    bad_guys.append(bad_guy)

#make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0, -260)
font = ("courier", 24, "bold")
pen.write("SCORE: {}".format(score), align= "center", font=font)


# functions
def go_left():
    player.direction = "left"


def go_right():
    player.direction = "right"


# moving our players with the keyboard
wn.listen()
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')

while True:
    wn.update()

    if player.direction == "left":
        x = player.xcor()
        x -= 1
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 1
        player.setx(x)
    # moving the good guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)

        if good_guy.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("SCORE: {}".format(score), align= "center", font=font)
    # moving the bad guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)

        if bad_guy.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 10
            pen.clear()
            pen.write("SCORE: {}".format(score), align= "center", font=font)

wn.mainloop()
