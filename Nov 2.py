from Myro import *

robot = getRobot()

#######
'''
SERVOS TO LEG:
4 = Leg 1
8 = Leg 2
12 = Leg 3
3 = Leg 4
7 = Leg 5
11 = Leg 6

FOR UP AND DOWN SERVOS:
6 = Leg 1
10 = Leg 2
14 = Leg 3
5 = Leg 4
9 = Leg 5
13 = Leg 6

'''
#######

#robot servos (RF-FB = rightFront-frontBack, RM-UD = rightMiddle-upDown, RB-FB = rightBack-frontBack)
RF_FB = 4 
RF_UD = 6
RM_FB = 8
RM_UD = 10 
RB_FB = 12
RB_UD = 14

LF_FB = 3
LF_UD = 5
LM_FB = 7
LM_UD = 9
LB_FB = 11
LB_UD = 13

def setServoPercent(servo,percent):
    print("In setServoPercent")
    if percent > 100 or percent < 0:
        print("no")
        return
    if servo == RF_UD or servo == RM_UD or servo == RB_UD:
        maxNum = 300
        minNum = 180
    elif servo == LF_UD or servo == LM_UD or servo == LB_UD:
        maxNum = 60
        minNum = 180
    elif servo == RF_FB or servo == LF_FB:
        maxNum = 240
        minNum = 180
    elif servo == RM_FB or servo == LM_FB:
        maxNum = 210
        minNum = 150
    elif servo == RB_FB or servo == LB_FB:
        maxNum = 175
        minNum = 115
    rangeOfValues = abs(maxNum - minNum)
    realPercent = percent * 0.01
    moveToValue = (realPercent * rangeOfValues) + minNum
    print("Move to:",moveToValue)
    setServo(servo,moveToValue)
 




def reboot(port):
    init(port,"Bioloid")
def right():
    turnLeft(4,3.75)

def left():
    turnRight(4,3.75)

def turnIntoDegree(servo):
    data = robot.getServo(servo)
    print(data)
    degree = (data[3]/1024)*(360)
    final = 360 - degree
    final = round(final,1)
    degree = round(degree,1)
    print(degree)
    print(final)
    
        
#######
'''
servos 14,10,6 are 360 on top and 0 on bottom
servos 5,9,13 are 0 on top and 360 on bottom
robot.flush - fixes weird issues
'''
#######

def rightLegsDown():
    robot.setServo(14,180)
    robot.setServo(10,180)
    robot.setServo(6,180)
    
def rightLegsUp():
    robot.setServo(14,300)
    robot.setServo(10,300)
    robot.setServo(6,300)
    
def leftLegsUp():
    robot.setServo(5,80)
    robot.setServo(9,80)
    robot.setServo(13,80)
    
def leftLegsDown():
    robot.setServo(5,180)
    robot.setServo(9,180)
    robot.setServo(13,180)

def allLegsDown():
    leftLegsDown()
    rightLegsDown()
    scorponokStrike()

def allLegsUp():
    leftLegsUp()
    rightLegsUp()
    scorponokReady()
        
def leftClawOpen():
    robot.setServo(1,220)
    
def leftClawClose():
    robot.setServo(1,150)
    
def rightClawOpen():
    robot.setServo(2,140)
    
def rightClawClose():
    robot.setServo(2,210)
    
#######
'''
servos 16,17,18 are the claw servos

'''
#######

def stingerBottomBackward():
    robot.setServo(16,200)

def stingerBottomForward():
    robot.setServo(16,270)
    
def stingerMiddleCurl():
    robot.setServo(17,260)
    
def stingerMiddleStraight():
    robot.setServo(17,190)
    
def stingerTopReady():
    robot.setServo(18,190)
    
def stingerTopStrike():
    robot.setServo(18,262)
    
def stingerTopThrow():
    robot.setServo(18,210)
    
def scorponokStrike():
    stingerBottomForward()
    stingerMiddleCurl()
    stingerTopStrike()
    
def scorponokThrow():
    stingerBottomForward()
    stingerMiddleCurl()
    stingerTopThrow()
    
def scorponokReady():
    stingerBottomBackward()
    stingerMiddleStraight()
    stingerTopReady()
    
#######
'''
Half Measurements

'''
#######

def rightLegsUpHalf():
    robot.setServo(14,220)
    robot.setServo(10,220)
    robot.setServo(6,220)
    
def leftLegsUpHalf():
    robot.setServo(5,140)
    robot.setServo(9,140)
    robot.setServo(13,140)
    
def leftClawOpenHalf():
    robot.setServo(1,220)
    
def leftClawCloseHalf():
    robot.setServo(1,150)
    
def rightClawOpenHalf():
    robot.setServo(2,140)
    
def rightClawCloseHalf():
    robot.setServo(2,210)
    
def scorponokSquatDown():
    leftLegsUpHalf()
    rightLegsUpHalf()
    

    
def scorponokSquatUp():
    leftLegsDown()
    rightLegsDown()
    
def DOSQUATS():
    for i in range(4):
        scorponokSquatDown()
        wait(.8)
        scorponokSquatUp()
        wait(.8)
        beep(1,16)
    beep(1,8)
    beep(1,12)
    



def default():
    setServo(5,180)
    setServo(9,180)
    setServo(13,180)
    wait(0.5)
    setServo(3,140)
    setServo(7,180)
    setServo(11,220)
    wait(0.5)
    setServo(14,180)
    setServo(10,180)
    setServo(6,180)
    wait(0.5)
    setServo(12,140)
    setServo(8,180)
    setServo(4,220)
    wait(0.5)
    scorponokStrike()
    wait(0.5)
    rightClawClose()
    leftClawClose()

def scopoForward():
    robot.setServo(6,220)    
    setServo(4,220)
    
def claws():
    leftClawOpen()
    wait(0.2)
    leftClawClose()
    wait(0.2)
    rightClawOpen()
    wait(0.2)
    rightClawClose()
    wait(0.2)

def scopoHiss():
    robot.setServo(9,140)
    robot.setServo(10,220)
    wait(0.5)
    robot.setServo(13,140)
    robot.setServo(14,220)
    wait(0.5)
    scorponokReady()    
    scorponokStrike()
    wait(0.5)
    claws()
    wait(0.5)
    claws()
"""

def walk():
    for i in range(3):  
        setServo(5,140)
        setServo(14,220)
        setServo(3,110)
        setServo(12,180)
        setServo(5,170)
        setServo(14,190)
        wait(0.5)    
        setServo(LB_UD,140)
        setServo(RF_UD,220)
        setServo(LB_FB,180)
        setServo(RF_FB,240)
        setServo(LB_UD,170)
        setServo(RF_UD,190)
        wait(0.5)
        setServo(LM_UD,160)
        setServo(RM_UD,200)
        setServo(LM_FB,160)
        setServo(RM_FB,200)
        setServo(LM_UD,170)
        setServo(RM_UD,190)
        wait(0.5)
        setServo(LB_FB,220)
        setServo(RB_FB,140)
"""
def walk():
    ###First Set
    setServoPercent(RM_UD,50)
    setServoPercent(RM_FB,100)
    setServoPercent(RM_UD,0)
    
    setServoPercent(LF_UD,00)
    """
    setServoPercent(LF_FB,100)
    setServoPercent(LF_UD,0)
    
    setServoPercent(LB_UD,66.66)
    setServoPercent(LB_FB,100)
    setServoPercent(LB_UD,0)
    ###Second Set
    setServoPercent(LM_UD,66.66)
    setServoPercent(LM_FB,100)
    setServoPercent(LM_UD,0)
    
    setServoPercent(
    setServoPercent(
    setServoPercent(
    
    setServoPercent(
    setServoPercent(
    setServoPercent(
    
   # setServo(RF_UD)
"""

    
