import turtle
import time

screen = turtle.Screen()
screen.title("کشیدن نام")
t = turtle.Turtle()
t.speed(1)

def draw_letter(x, y, letter, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.write(letter, align="center", font=("Arial", 24, "normal"))
    time.sleep(1)

name = "Welcome To My GitHub"
x_position = -160
y_position = 0

for letter in name:
    if letter == ' ':
        x_position += 20
    elif letter == 'o':
        draw_letter(x_position, y_position, letter, "red")
        x_position += 30
    else:
        draw_letter(x_position, y_position, letter, "blue")
        x_position += 30
    if x_position > 200:
        time.sleep(2)
        t.clear()
        x_position = -160

screen.exitonclick()
