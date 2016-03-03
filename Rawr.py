from Myro import *
from Graphics import *

###Room
win = Window("Room for Jeff", 900,900)
floor = Rectangle((0,450),(900,900))
floor.fill=Color("burlywood")
floor.draw(win)
win.setBackground(Color("Blue"))
###Door2
Door = Rectangle((350,200),(500,450))
Door.fill=Color("saddlebrown")
Door.draw(win)
Doorknob = Circle((475,325),15)
Doorknob.fill=Color("Gold")
Doorknob.draw(win)
###Door1
Door2 = Rectangle((50,200),(200,450))
Door2.fill=Color("saddlebrown")
Door2.draw(win)
Doorknob2 = Circle((175,325),15)
Doorknob2.fill=Color("Gold")
Doorknob2.draw(win)
Door2.tag="Brown"
###Door3
Door = Rectangle((650,200),(800,450))
Door.fill=Color("saddlebrown")
Door.draw(win)
Doorknob = Circle((775,325),15)
Doorknob.fill=Color("Gold")
Doorknob.draw(win)
###OpenDoor2
OpenDoor2 = Rectangle((50,200),(75,450))
OpenDoor2.fill.alpha=0
OpenDoor2.outline.alpha=0
OpenDoor2.draw(win)
###keypress
def handleMouseUp(obj, event):
    print("Up")

def handleMouseDown(obj, event):
    print(event.x,event.y)
    print(Door2.hit(event.x,event.y))
    if Door2.hit(event.x,event.y) and Door2.tag=="Brown":
        print("got here")
        Door2.fill=Color("White")
        Door2.tag="White"
        win.canvas.shapes.Remove(Doorknob2)
        win.canvas.shapes.Add(OpenDoor2)
        OpenDoor2.fill=Color("saddlebrown")
    elif Door2.hit(event.x,event.y) and Door2.tag=="White":
        Door2.fill=Color("saddlebrown")
        Door2.tag="Brown"
        win.canvas.shapes.Remove(OpenDoor2)
        print("Help")
        win.canvas.shapes.Add(Doorknob2)

        

def handleMouseMovement(obj, event):
    print("Movement")

#onMouseMovement(handleMouseMovement)
#onMouseUp(handleMouseUp)
onMouseDown(handleMouseDown)