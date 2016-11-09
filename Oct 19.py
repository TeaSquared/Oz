from Myro import *

robot = getRobot()

def reboot(port):
    init(port,"Bioloid")
def right():
    turnLeft(4,3.75)

def left():
    turnRight(4,3.75)

def turnToDegree(servo):
    data = robot.getServo(servo)
    print(data)
    degree = (data[2]/1024)*(360)
    final = 360 - degree
    final = round(final,1)
    degree = round(degree,1)
    print(degree)
    print(final)
    
        
#######
'''
servos 14,10,6 are 360 on top and 0 on bottom
servos 5,9,13 are 0 on top and 360 on bottom
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
def leftClawOpen():
    robot.setServo(1,220)
def leftClawClose():
    robot.setServo(1,150)
def rightClawOpen():
    robot.setServo(2,140)
def rightClawClose():
    robot.setServo(2,220)
