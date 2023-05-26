import turtle
import random

Screen = turtle.Screen()
NameTurtle = turtle.Turtle()
ScoreTurtle = turtle.Turtle()
CounterTurtle = turtle.Turtle()
isGameOver = False
Player_Score = 0
Screen.bgcolor("#A9A9A9")
Screen.title("Hello World!")
RandomPositionsList = []
RandomBait= []

def Bait(xValue,yValue):
    MyBait= turtle.Turtle()
    def click(xValue, yValue):
        global Player_Score
        if Player_Score > 0:
            Player_Score -= 1
            ScoreTurtle.clear()
            ScoreTurtle.write("SCORE: {}".format(Player_Score), move=False, align='center',font=('Georgia ', 20, 'bold'))
        else:
            ScoreTurtle.clear()
            ScoreTurtle.write("SCORE: {}".format(Player_Score), move=False, align='center',font=('Georgia ', 20, 'bold'))

    MyBait.onclick(click)
    MyBait.penup()
    MyBait.shape("turtle")
    MyBait.color("#1D841F")
    MyBait.shapesize(3,3)
    MyBait.setposition(xValue*80,yValue*80)
    MyBait.pendown()
    RandomBait.append(MyBait)

def TurtleShape(xValue, yValue):
    MyTurtle = turtle.Turtle()

    def click(xValue, yValue):

        global Player_Score
        Player_Score += 1
        ScoreTurtle.clear()
        ScoreTurtle.write("SCORE: {}".format(Player_Score), move=False, align='center', font=('Georgia ', 20, 'bold'))


    MyTurtle.onclick(click)
    MyTurtle.penup()
    MyTurtle.shape("turtle")
    MyTurtle.color("#006400")
    MyTurtle.shapesize(3, 3)
    MyTurtle.setposition(xValue*100,yValue*100)
    MyTurtle.pendown()
    RandomPositionsList.append(MyTurtle)
def NameOfGame():
    NameTurtle.hideturtle()
    NameTurtle.color("#006400")
    NameTurtle.penup()
    height = Screen.window_height() / 2
    yCor = height - (height / 10)
    NameTurtle.setposition(0, yCor)
    NameTurtle.write("! ! C A T C H  T H E  T U R T L E ! !", move=False, align='center', font=('Georgia ', 20, 'bold'))
def PlayerScore():
    ScoreTurtle.hideturtle()
    ScoreTurtle.color("pink")
    ScoreTurtle.penup()
    height = Screen.window_height() / 2
    yCor = height - (height / 10)
    ScoreTurtle.setposition(0, yCor - 50)
    ScoreTurtle.write("SCORE: {}".format(Player_Score), move=False, align='center', font=('Georgia ', 20, 'bold'))
X_list = list(range(-3,3))
Y_list = list(range(-3,3))
def turtle_positions():
    for xValue in X_list:

        for yValue in Y_list:
            Bait(xValue,yValue)
            TurtleShape(xValue,yValue)
def hideBaits():
    for i in RandomBait:
        i.hideturtle()
def hideTurtles():
    for i in RandomPositionsList:
        i.hideturtle()

def RandomlyShowTurtle():

    if  not isGameOver:
        print("if random")
        hideTurtles()
        hideBaits()
        random.choice(RandomPositionsList).showturtle()
        random.choice(RandomBait).showturtle()
        Screen.ontimer(RandomlyShowTurtle, 100)
    else:
        hideTurtles()
        hideBaits()
def Counter(t):
    print("counter")
    CounterTurtle.hideturtle()
    CounterTurtle.penup()
    height = Screen.window_height() / 2
    yCor = height - (height / 10)
    CounterTurtle.setposition(0, yCor - 100)
    CounterTurtle.clear()


    if t > 0:
        print("if")
        CounterTurtle.clear()
        CounterTurtle.color("red")
        Screen.ontimer(lambda: Counter(t - 1), 1000)
        CounterTurtle.write("Remaining time:{}".format(t), move=False, align="center", font=('Georgia ', 20, 'bold'))
    else:
        print("else")
        global isGameOver
        isGameOver = True
        CounterTurtle.clear()
        CounterTurtle.color("#C71585")
        CounterTurtle.write("G A M E   O V E R :(", align="center", font=('Georgia ', 20, 'bold'))
        hideTurtles()
def StartTheGame():
    global isGameOver
    isGameOver = False
    Counter(15)
    turtle.tracer(0)
    NameOfGame()
    PlayerScore()
    turtle_positions()
    hideTurtles()
    hideBaits()
    RandomlyShowTurtle()
    turtle.tracer(1)





StartTheGame()
turtle.mainloop()