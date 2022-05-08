# 科赫曲线
import turtle

def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            # 递归调用
            koch(size/3, n-1)

def drawCurLine():
    turtle.setup(800, 400)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600, 3)
    turtle.hideturtle()

def drawSnow():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()

def main():
    drawSnow()

main()
