from Myro import *

robot = getRobot()

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
    
def reboot(port):
    init(port,"Bioloid")
    
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
    if servo == LF_UD or servo == LM_UD or servo == LB_UD:
        percent = (100 - percent)
        
    if servo == LF_FB or servo == LM_FB or servo == LB_FB:
        percent = (100 - percent)
        
    if servo == RF_UD or servo == RM_UD or servo == RB_UD:
        maxNum = 300
        minNum = 180
        
    elif servo == LF_UD or servo == LM_UD or servo == LB_UD:
        maxNum = 60
        minNum = 180
        
    elif servo == RF_FB:
        maxNum = 240
        minNum = 180
     #   
    elif servo == LF_FB:
        maxNum = 240
        minNum = 120
        
    elif servo == RM_FB or servo == LM_FB:
        maxNum = 210
        minNum = 150
        
    elif servo == RB_FB:
        maxNum = 175
        minNum = 115
    
    elif servo == LB_FB:
        maxNum = 175
        minNum = 240
        
    rangeOfValues = abs(maxNum - minNum)
    realPercent = percent * 0.01
    
    if servo == LF_UD or servo == LM_UD or servo == LB_UD or servo == LB_FB :
        minNum = maxNum
    
        
    moveToValue = (realPercent * rangeOfValues) + minNum
    print("Range:", rangeOfValues)
    print("Move to:",moveToValue)
    setServo(servo,moveToValue)
 
