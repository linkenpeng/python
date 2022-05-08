import turtle, time

def drawGap():
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write("年", font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write("月", font=("Arial", 18, "normal"))
        elif i == '+':
            turtle.write("日", font=("Arial", 18, "normal"))
        else:
            print(i)
            drawDigit(i)
            
def printDigit(date):
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(date)
    turtle.hideturtle()
    turtle.done()

def main():
    date = time.strftime("%Y-%m=%d+", time.gmtime())
    print(date)
    printDigit(date)

main()








