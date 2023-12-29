import turtle
import time

def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_birthday_card(name):
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    turtle.color("blue")
    turtle.write(f"Happy Birthday, {name}!", font=("Arial", 16, "bold"))

    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.color("red")
    turtle.write("Wishing you a fantastic day filled with joy and laughter.", font=("Arial", 12, "italic"))

    turtle.penup()
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.color("green")
    turtle.write("Let the celebrations begin!", font=("Arial", 14, "bold"))

def draw_cake():
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()

    # Draw cake
    turtle.color("brown")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.end_fill()

    # Draw candles
    for i in range(5):
        turtle.penup()
        turtle.goto(20 * i - 40, -130)
        turtle.pendown()
        turtle.color("yellow")
        turtle.begin_fill()
        draw_star(10)
        turtle.end_fill()

def main():
    turtle.speed(2)
    turtle.bgcolor("pink")

    draw_birthday_card("Trishia")
    time.sleep(2)
    
    turtle.clear()

    draw_cake()
    time.sleep(2)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
