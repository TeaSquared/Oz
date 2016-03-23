from Myro import *
from Graphics import *

class Areas:
    def __init__(self):
        self.area = Rectangle((300,570),(580,290))
        self.status = "Not Chosen"
        self.area.draw(win)
    def resizeArea(self,bottomLeftX,bottomLeftY,topRightX,topRightY):
        win.canvas.shapes.Remove(self.area)
        self.area = Rectangle((bottomLeftX,bottomLeftY),(topRightX,topRightY))
        self.area.draw(win)
        self.topRightX=topRightX
        self.topRightY=topRightY
        self.bottomLeftX=bottomLeftX
        self.bottomLeftY=bottomLeftY

win = Window("Tic-Tac-Toe", 900, 900)
win.setBackground(Color("Snow"))

###Even or Odd
def isEven(number):
    return number % 2 == 0
Counter = 2
###Board Set-Up

line1 = RoundedRectangle((280,50),(300,850),10)
line1.fill=Color("Black")
line1.draw(win)

line2 = RoundedRectangle((580,50),(600,850),10)
line2.fill=Color("Black")
line2.draw(win)

line3 = RoundedRectangle((50,270),(850,290),10)
line3.fill=Color("Black")
line3.draw(win)

line4 = RoundedRectangle((50,570),(850,590),10)
line4.fill=Color("Black")
line4.draw(win)

###Defining Areas

centerArea = Areas()
centerArea.fill=Color("Purple")

centerRightArea = Areas()
centerRightArea.resizeArea(600,570,900,290)
centerRightArea.fill=Color("Purple")

centerLeftArea = Areas()
centerLeftArea.resizeArea(0,570,280,290)
centerLeftArea.fill=Color("Purple")

centerUpArea = Areas()
centerUpArea.resizeArea(300,270,580,0)
centerUpArea.area.fill=Color("Green")

centerUpperRightArea = Areas()
centerUpperRightArea.resizeArea(600,270,900,0)
centerUpperRightArea.area.fill=Color("Green")

centerUpperLeftArea = Areas()
centerUpperLeftArea.resizeArea(280,270,0,0)
centerUpperLeftArea.area.fill=Color("Green")

centerLowerArea = Areas()
centerLowerArea.resizeArea(600,590,900,900)
centerLowerArea.area.fill=Color("Red")

centerLowerRightArea = Areas()
centerLowerRightArea.resizeArea(300,590,580,900)
centerLowerRightArea.area.fill=Color("Red")

centerLowerLeftArea = Areas()
centerLowerLeftArea.resizeArea(0,590,280,900)
centerLowerLeftArea.area.fill=Color("Red")

###X and O
objectX = Picture("X.jpg")
objectO = Picture("O.jpg")

### Selection

def handleMouseDown(obj, event): 
        for Tic in Areas:
            print("Check")
            if Tic.area.hit(event.x,event.y):
                print("Hit")
                if isEven(Counter) == True:
                    objectX.setX((Tic.topRightX)-(Tic.bottomLeftX))
                    objectX.setY((Tic.topRightY)-(Tic.bottomLeftY))
                    objectX.draw(win)
                    Print("Created X")
                    Counter = Counter+1
                if isEven(Counter) == False:
                    objectO.setX((Tic.topRightX)-(Tic.bottomLeftX))
                    objectO.setY((Tic.topRightY)-(Tic.bottomLeftY))
                    objectO.draw(win)
                
win.onMouseDown(handleMouseDown)