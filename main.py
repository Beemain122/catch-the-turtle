from turtle import *
from random import randint

# ===== Настройка окна =====
screen = Screen()
screen.setup(width=600, height=400)
screen.title("Снайперская Черепаха")

t = Turtle()
t.shape("turtle")
t.color("red")
t.speed(5)
t.penup()  # Чтобы не рисовать линии

# ===== Переменные =====
t.i = 1
max_score = 3

# ===== Функция при клике =====
def catch(x, y):
    t.write("AЙ СНАЙПНУЛ В ПОЛЬОТЕ!", font=("Sansita", 12, "bold"))
    t.goto(randint(-250, 250), randint(-150, 150))
    t.i += 1
    if t.i > max_score:
        t.clear()
        t.write("ПЕРЕМОГА БУДЕ!", font=("Sansita", 16, "bold"))
        t.hideturtle()

t.onclick(catch)

# ===== Функция движения черепахи =====
def move_turtle():
    if t.i <= max_score:
        t.clear()
        t.goto(randint(-250, 250), randint(-150, 150))
        screen.ontimer(move_turtle, 1000)  # вызываем снова через 1 сек

# запускаем движение
move_turtle()

screen.mainloop()
