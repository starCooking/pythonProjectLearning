import turtle
import time

# 设置屏幕
wn = turtle.Screen()
wn.title("贪吃蛇游戏")
wn.bgcolor("green")
wn.setup(width=600, height=600)

# 设置蛇头
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# 设置食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,100)

# 设置移动函数
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 设置控制函数
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

# 绑定控制函数
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# 主循环
while True:
    wn.update()
    # 如果吃到食物
    if head.distance(food) < 20:
        x = food.xcor()
        y = food.ycor()
        food.goto(x,y)
    move()
    time.sleep(0.1)

wn.mainloop()