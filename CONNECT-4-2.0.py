import turtle

myTurtle = turtle.Turtle()
myTurtle.speed(-1)
myTurtle.shape("circle")
squareSize = 50
length = 7
size = 6

def drawSquare(myTurtle,squareSize):
    for i in range(4):
        myTurtle.fd(squareSize)
        myTurtle.right(90)

def drawRow(myTurtle,length,squareSize):
    for i in range(length):
        drawSquare(myTurtle,squareSize)
        myTurtle.fd(squareSize)
       
def drawGrid(myTurtle,size,squareSize):
    for i in range(1,size + 1):
        drawRow(myTurtle,length,squareSize)
        myTurtle.penup()
        myTurtle.goto(0,0)
        myTurtle.pendown()
        myTurtle.right(90)
        myTurtle.fd(squareSize*i)
        myTurtle.left(90)
    myTurtle.penup()
    myTurtle.goto(0,50)

def redPiece():
    myTurtle.fillcolor("red")
    myTurtle.shape("circle")
    myTurtle.pensize(100)

    
def yellowPiece():
    myTurtle.fillcolor("yellow")
    myTurtle.shape("circle")
    myTurtle.pensize(100)
    

 
def playGame():

    for i in range(21):
        player_1 = yellowPiece()                ###Player 1 Starts here
        p1move_piece = int(input("Player 1, Pick row 1 - 7:"))
        
        while(p1move_piece < 1 or p1move_piece > 7):
            print("Try again")
            p1move_piece = int(input("Pick row 1 - 7:"))
        
        if p1move_piece == 1:
            myTurtle.penup()
            myTurtle.goto(25,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_2 = redPiece()


        elif p1move_piece == 2:
            myTurtle.penup()
            myTurtle.goto(75,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_2 = redPiece()

        elif p1move_piece == 3:
            myTurtle.penup()
            myTurtle.goto(125,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_2 = redPiece()
            
        elif p1move_piece == 4:
            myTurtle.penup()
            myTurtle.goto(175,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_2 = redPiece()
            
        elif p1move_piece == 5:
            myTurtle.penup()
            myTurtle.goto(225,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_2 = redPiece()
            
        elif p1move_piece == 6:
            myTurtle.penup()
            myTurtle.goto(275,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_2 = redPiece()
            
        elif p1move_piece == 7:
            myTurtle.penup()
            myTurtle.goto(325,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_2 = redPiece()

        player_2 = redPiece()                       ###Player 2 Starts here
        p2move_piece = int(input("Player 2,Pick row 1 - 7:"))

        while(p2move_piece < 1 or p2move_piece > 7):
            print("Try again")
            p2move_piece = int(input("Player 2,Pick row 1 - 7:"))
        
        if p2move_piece == 1:
            myTurtle.penup()
            myTurtle.goto(25,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_1 = yellowPiece()

        elif p2move_piece == 2:
            myTurtle.penup()
            myTurtle.goto(75,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_1 = yellowPiece()

        elif p2move_piece == 3:
            myTurtle.penup()
            myTurtle.goto(125,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_1 = yellowPiece()
            
        elif p2move_piece == 4:
            myTurtle.penup()
            myTurtle.goto(175,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_1 = yellowPiece()
            
        elif p2move_piece == 5:
            myTurtle.penup()
            myTurtle.goto(225,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_1 = yellowPiece()
            
        elif p2move_piece == 6:
            myTurtle.penup()
            myTurtle.goto(275,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_1 = yellowPiece()
            
        elif p2move_piece == 7:
            myTurtle.penup()
            myTurtle.goto(325,-275)
            myTurtle.stamp()
            myTurtle.goto(0,50)
            player_1 = yellowPiece()
            
            
drawGrid(myTurtle,size,squareSize)
playGame()*21
